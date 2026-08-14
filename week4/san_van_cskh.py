"""
san_van_cskh.py — Sàn Vận Hành CSKH Tự Động
Engine chính: chạy 4 nhân viên agent song song theo lịch định kỳ.

Cách chạy:
    python san_van_cskh.py

Biến môi trường:
    CHAY_MOI_N_PHUT=30       (mặc định: 30)
    CHAY_24H=false           (mặc định: false — chỉ chạy giờ hành chính)
    DUNG_NHIEU_MODEL=false   (mặc định: false — tất cả dùng gpt-4o-mini)
"""
import asyncio, os
from datetime import datetime
from dotenv import load_dotenv
from agents import add_trace_processor
from nhan_vien import NhanVien
from tracers_shop import LogTracer
from khoi_dong import CHIEN_LUOC_BAN_DAU, xem_chuc_vu

load_dotenv(override=True)

# ── Cấu hình từ .env ──────────────────────────────────────────────────────
CHAY_MOI_N_PHUT = int(os.getenv("CHAY_MOI_N_PHUT", "30"))
CHAY_24H        = os.getenv("CHAY_24H",        "false").strip().lower() == "true"
DUNG_NHIEU_MODEL = os.getenv("DUNG_NHIEU_MODEL", "false").strip().lower() == "true"

# ── Tên 4 nhân viên và model tương ứng ────────────────────────────────────
TEN_NHAN_VIEN = ["An", "Binh", "Chi", "Dung"]

if DUNG_NHIEU_MODEL:
    # Dùng nhiều LLM providers — cần API keys tương ứng trong .env
    # An: OpenAI (default)
    # Binh: DeepSeek (rẻ, giỏi tiếng Việt)
    # Chi: OpenAI (stable)
    # Dung: Gemini (fast)
    MODEL_NAMES = [
        "gpt-4o-mini",
        "deepseek-chat",
        "gpt-4o-mini",
        "gemini-2.5-flash-preview-04-17",
    ]
    TEN_MODEL_NGAN = ["GPT-4o Mini", "DeepSeek V3", "GPT-4o Mini", "Gemini 2.5 Flash"]
else:
    MODEL_NAMES   = ["gpt-4o-mini"] * 4
    TEN_MODEL_NGAN = ["GPT-4o Mini"] * 4


def _dang_gio_hanh_chinh() -> bool:
    """Kiểm tra có đang trong giờ hành chính VN không (8h-18h, T2-T7)."""
    now = datetime.now()
    return now.weekday() < 6 and 8 <= now.hour < 18  # Mon-Sat, 8am-6pm


def tao_nhan_vien() -> list[NhanVien]:
    """Tạo 4 nhân viên agent với model và chiến lược riêng."""
    nhan_vien = []
    for ten, model in zip(TEN_NHAN_VIEN, MODEL_NAMES):
        chuc_vu = xem_chuc_vu(ten)
        nv = NhanVien(ten=ten, chuc_vu=chuc_vu, model=model)
        nhan_vien.append(nv)
    return nhan_vien


async def chay_theo_lich():
    """
    Vòng lặp chính: chạy 4 nhân viên song song mỗi N phút.

    Pattern tương tự trading_floor.py:
        while True:
            await asyncio.gather(*[trader.run() for trader in traders])
            await asyncio.sleep(N * 60)
    """
    # Đăng ký custom tracer — intercept trace events → ghi SQLite
    add_trace_processor(LogTracer())

    nhan_vien = tao_nhan_vien()

    print("\n" + "═" * 60)
    print("  SÀN VẬN HÀNH CSKH TỰ ĐỘNG — TrendVN Shop")
    print("═" * 60)
    for nv, model in zip(nhan_vien, TEN_MODEL_NGAN):
        print(f"  {nv.ten:<8} ({nv.chuc_vu}) — {model}")
    print(f"\n  Chu kỳ: mỗi {CHAY_MOI_N_PHUT} phút")
    print(f"  Chạy 24h: {'Có' if CHAY_24H else 'Không (chỉ giờ hành chính 8h-18h T2-T7)'}")
    print("═" * 60 + "\n")

    vong = 0
    while True:
        vong += 1
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M")

        if CHAY_24H or _dang_gio_hanh_chinh():
            print(f"\n[{now_str}] Vòng #{vong} — Khởi động 4 nhân viên song song...")

            # asyncio.gather: chạy TẤT CẢ song song
            # Khi một agent đang chờ IO (API, MCP), agent khác tiếp tục chạy
            await asyncio.gather(*[nv.run() for nv in nhan_vien])

            print(f"[{now_str}] Vòng #{vong} hoàn tất — ngủ {CHAY_MOI_N_PHUT} phút...")
        else:
            print(f"[{now_str}] Ngoài giờ hành chính — bỏ qua (set CHAY_24H=true để chạy)")

        await asyncio.sleep(CHAY_MOI_N_PHUT * 60)


if __name__ == "__main__":
    print(f"Khởi động scheduler — chạy mỗi {CHAY_MOI_N_PHUT} phút")
    asyncio.run(chay_theo_lich())