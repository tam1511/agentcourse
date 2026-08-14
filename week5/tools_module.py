"""
tools_module.py
Toàn bộ tools cho Trợ Lý AI Doanh Nghiệp VN.
Thêm tool mới vào đây — agent tự động nhận được.
"""

import os
import subprocess
import tempfile
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv(override=True)

# ─── Cấu hình ────────────────────────────────────────────────────────
# Thư mục sandbox — agent CHỈ được phép làm việc trong này
SANDBOX_DIR = Path("./sandbox_workspace")
SANDBOX_DIR.mkdir(exist_ok=True)

serper = GoogleSerperAPIWrapper()


# ─── Tool 1: Web Search ──────────────────────────────────────────────

@tool
def tim_kiem_web(truy_van: str) -> str:
    """
    Tìm kiếm thông tin trên internet.
    Dùng khi cần: giá cả thị trường, tin tức ngành, thông tin đối thủ,
    xu hướng kinh doanh, số liệu thống kê.
    Tham số truy_van: câu hỏi hoặc từ khóa tìm kiếm, nên dùng tiếng Việt
    hoặc tiếng Anh tùy ngữ cảnh.
    """
    try:
        ket_qua = serper.run(truy_van)
        return f"Kết quả tìm kiếm cho '{truy_van}':\n{ket_qua}"
    except Exception as e:
        return f"Lỗi khi tìm kiếm: {str(e)}"


# ─── Tool 2: Đọc file ────────────────────────────────────────────────

@tool
def doc_file(ten_file: str) -> str:
    """
    Đọc nội dung một file văn bản trong thư mục làm việc.
    Hỗ trợ: .txt, .md, .csv, .json, .py
    Tham số ten_file: tên file (ví dụ: 'bao_cao.md', 'du_lieu.csv')
    KHÔNG bao gồm đường dẫn tuyệt đối — chỉ tên file.
    """
    duong_dan = SANDBOX_DIR / ten_file

    # Bảo mật: không cho phép đi ra ngoài sandbox
    try:
        duong_dan = duong_dan.resolve()
        if not str(duong_dan).startswith(str(SANDBOX_DIR.resolve())):
            return "Lỗi: Không được phép truy cập file ngoài thư mục làm việc."
    except Exception:
        return "Lỗi: Đường dẫn file không hợp lệ."

    if not duong_dan.exists():
        # List các file có sẵn để agent biết
        cac_file = [f.name for f in SANDBOX_DIR.iterdir() if f.is_file()]
        return (f"File '{ten_file}' không tồn tại.\n"
                f"Các file hiện có: {', '.join(cac_file) if cac_file else 'Chưa có file nào.'}")

    try:
        noi_dung = duong_dan.read_text(encoding="utf-8")
        so_ky_tu = len(noi_dung)
        # Giới hạn 8000 ký tự để tránh context quá dài
        if so_ky_tu > 8000:
            noi_dung = noi_dung[:8000] + f"\n\n[... Đã cắt bớt. File có {so_ky_tu} ký tự tổng cộng]"
        return f"Nội dung file '{ten_file}':\n\n{noi_dung}"
    except UnicodeDecodeError:
        return f"Không thể đọc file '{ten_file}' — có thể là file nhị phân."
    except Exception as e:
        return f"Lỗi khi đọc file: {str(e)}"


# ─── Tool 3: Ghi file ────────────────────────────────────────────────

@tool
def ghi_file(ten_file: str, noi_dung: str, che_do: str = "ghi_moi") -> str:
    """
    Tạo hoặc cập nhật một file văn bản trong thư mục làm việc.
    Tham số:
    - ten_file: tên file cần ghi (ví dụ: 'bao_cao_q1.md')
    - noi_dung: nội dung cần ghi vào file
    - che_do: 'ghi_moi' (xóa và ghi lại từ đầu) hoặc 'them_vao' (nối thêm vào cuối)
    Định dạng khuyến nghị: dùng .md cho báo cáo, .csv cho dữ liệu, .txt cho ghi chú.
    """
    duong_dan = SANDBOX_DIR / ten_file

    try:
        duong_dan = duong_dan.resolve()
        if not str(duong_dan).startswith(str(SANDBOX_DIR.resolve())):
            return "Lỗi bảo mật: Không được ghi file ngoài thư mục làm việc."
    except Exception:
        return "Lỗi: Tên file không hợp lệ."

    try:
        mode = "a" if che_do == "them_vao" else "w"
        with open(duong_dan, mode, encoding="utf-8") as f:
            f.write(noi_dung)
        kich_thuoc = duong_dan.stat().st_size
        return (f"Đã {'thêm vào' if che_do == 'them_vao' else 'ghi'} file '{ten_file}' "
                f"thành công. Kích thước: {kich_thuoc:,} bytes.")
    except Exception as e:
        return f"Lỗi khi ghi file: {str(e)}"


# ─── Tool 4: Liệt kê files ───────────────────────────────────────────

@tool
def liet_ke_files() -> str:
    """
    Liệt kê tất cả files trong thư mục làm việc hiện tại.
    Dùng khi cần biết có những file nào đã được tạo.
    Không cần tham số đầu vào.
    """
    cac_file = list(SANDBOX_DIR.iterdir())
    if not cac_file:
        return "Thư mục làm việc hiện đang trống."

    danh_sach = []
    for f in sorted(cac_file):
        if f.is_file():
            kich_thuoc = f.stat().st_size
            danh_sach.append(f"  {f.name} ({kich_thuoc:,} bytes)")

    return "Files trong thư mục làm việc:\n" + "\n".join(danh_sach)


# ─── Tool 5: Chạy Python (có sandbox) ───────────────────────────────

@tool
def chay_python(code: str) -> str:
    """
    Chạy đoạn code Python và trả về output.
    QUAN TRỌNG: Phải dùng print() để nhận kết quả.
    Ví dụ đúng: print(2 + 2)  →  trả về "4"
    Ví dụ sai: 2 + 2  →  không trả về gì
    Dùng khi: tính toán số liệu, xử lý dữ liệu, tạo thống kê.
    Giới hạn: timeout 15 giây, không có internet access.
    Các thư viện có sẵn: math, statistics, json, csv, datetime, re
    """
    # Thêm import an toàn vào đầu code
    code_an_toan = """
import math
import statistics
import json
import csv
import re
from datetime import datetime, date, timedelta
from collections import Counter, defaultdict

# Code của agent:
""" + code

    try:
        # Chạy trong subprocess với timeout — an toàn hơn exec()
        ket_qua = subprocess.run(
            ["python", "-c", code_an_toan],
            capture_output=True,
            text=True,
            timeout=15,
            # Không cho access internet hay file system nhạy cảm
            env={
                "PATH": os.environ.get("PATH", ""),
                "PYTHONPATH": os.environ.get("PYTHONPATH", "")
            }
        )

        if ket_qua.returncode == 0:
            output = ket_qua.stdout.strip()
            return output if output else "Code chạy thành công nhưng không có output. Hãy thêm print()."
        else:
            loi = ket_qua.stderr.strip()
            # Rút gọn traceback cho dễ đọc
            dong_loi = loi.split("\n")
            loi_ngan = "\n".join(dong_loi[-3:]) if len(dong_loi) > 3 else loi
            return f"Lỗi Python:\n{loi_ngan}"

    except subprocess.TimeoutExpired:
        return "Timeout: Code chạy quá 15 giây. Hãy tối ưu lại."
    except Exception as e:
        return f"Không thể chạy code: {str(e)}"


# ─── Tool 6: Tính toán nhanh ─────────────────────────────────────────

@tool
def tinh_toan(bieu_thuc: str) -> str:
    """
    Tính toán biểu thức toán học đơn giản một cách an toàn.
    Ví dụ: '150000 * 0.1 + 5000', '(doanh_thu - chi_phi) / doanh_thu * 100'
    Tham số bieu_thuc: biểu thức toán học thuần túy, không có code phức tạp.
    Dùng cho: tính lợi nhuận, tỷ lệ phần trăm, ROI, các phép tính tài chính đơn giản.
    """
    import math
    # Whitelist các ký tự được phép — bảo mật
    cac_ky_tu_cho_phep = set("0123456789+-*/().,%^ eiπ")
    cac_ham_cho_phep = {
        "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
        "abs": abs, "round": round, "min": min, "max": max,
        "pi": math.pi, "e": math.e
    }

    try:
        ket_qua = eval(
            bieu_thuc.replace("^", "**").replace(",", ""),
            {"__builtins__": {}},
            cac_ham_cho_phep
        )
        if isinstance(ket_qua, float):
            return f"{bieu_thuc} = {ket_qua:,.4f}"
        return f"{bieu_thuc} = {ket_qua:,}"
    except ZeroDivisionError:
        return "Lỗi: Chia cho 0."
    except Exception as e:
        return f"Không thể tính: {str(e)}. Hãy dùng tool chay_python cho phép tính phức tạp hơn."


# ─── Tập hợp tất cả tools ────────────────────────────────────────────

def lay_tat_ca_tools() -> list:
    """
    Trả về danh sách tất cả tools.
    Thêm tool mới vào list này để agent tự động nhận được.
    """
    return [
        tim_kiem_web,
        doc_file,
        ghi_file,
        liet_ke_files,
        chay_python,
        tinh_toan,
    ]


def lay_mo_ta_tools() -> str:
    """Trả về mô tả ngắn gọn về tất cả tools — dùng trong system prompt."""
    tools = lay_tat_ca_tools()
    mo_ta = []
    for t in tools:
        mo_ta.append(f"- {t.name}: {t.description.split(chr(10))[0]}")
    return "\n".join(mo_ta)