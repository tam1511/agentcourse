"""
thong_bao_server.py — MCP Server thông báo nội bộ
Lưu log vào SQLite + gọi n8n webhook nếu có cấu hình.
Không cần Pushover hay bất kỳ service trả phí nào.
"""
import os, sqlite3
from datetime import datetime
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv(override=True)

DB_PATH     = "thong_bao.db"
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")   # Tùy chọn — để trống nếu không có n8n

def _init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS log_thong_bao (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_agent TEXT,
            loai      TEXT,
            noi_dung  TEXT,
            tao_luc   TEXT
        )
    """)
    conn.commit()
    conn.close()

_init_db()

mcp = FastMCP("thong_bao")


@mcp.tool()
def gui_thong_bao(ten_agent: str, loai: str, noi_dung: str) -> str:
    """Gửi thông báo nội bộ và lưu vào log. Dùng sau khi hoàn thành task quan trọng.

    Args:
        ten_agent: Tên agent gửi thông báo — ví dụ: "Agent CSKH", "Agent Đơn Hàng"
        loai: Loại thông báo — "hoan_thanh", "canh_bao", "bao_cao", "loi"
        noi_dung: Nội dung thông báo ngắn gọn (tối đa 200 ký tự)
    """
    tao_luc = datetime.now().isoformat()

    # Lưu vào SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO log_thong_bao (ten_agent, loai, noi_dung, tao_luc) VALUES (?,?,?,?)",
        (ten_agent, loai, noi_dung, tao_luc)
    )
    conn.commit()
    conn.close()

    # In ra console (visible trong Jupyter)
    icon = {"hoan_thanh": "✓", "canh_bao": "⚠", "bao_cao": "📊", "loi": "✗"}.get(loai, "•")
    print(f"\n[THÔNG BÁO] {icon} [{ten_agent}] {noi_dung}")

    # Gọi n8n webhook nếu có cấu hình
    if WEBHOOK_URL:
        try:
            import httpx
            httpx.post(WEBHOOK_URL, json={
                "agent": ten_agent, "loai": loai,
                "noi_dung": noi_dung, "tao_luc": tao_luc
            }, timeout=5)
        except Exception:
            pass  # Webhook fail không làm crash tool

    return f"Đã ghi thông báo: {noi_dung}"


@mcp.tool()
def xem_log_thong_bao(gioi_han: int = 10) -> list:
    """Xem lịch sử thông báo gần nhất.

    Args:
        gioi_han: Số lượng thông báo muốn xem (mặc định: 10)
    """
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT ten_agent, loai, noi_dung, tao_luc FROM log_thong_bao "
        "ORDER BY id DESC LIMIT ?", (gioi_han,)
    ).fetchall()
    conn.close()
    return [
        {"agent": r[0], "loai": r[1], "noi_dung": r[2], "tao_luc": r[3]}
        for r in rows
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")