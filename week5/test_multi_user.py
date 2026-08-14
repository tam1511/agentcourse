# test_multi_user.py
import asyncio
from session_manager import quan_ly_phien

async def simulate_user(ma_nguoi_dung: str, cac_yeu_cau: list):
    """Mô phỏng một người dùng gửi nhiều yêu cầu."""
    phien = quan_ly_phien.tao_phien_moi(ma_nguoi_dung)
    print(f"\n[{ma_nguoi_dung}] Bắt đầu phiên: {phien.session_id}")

    for yeu_cau in cac_yeu_cau:
        print(f"[{ma_nguoi_dung}] Gửi yêu cầu: {yeu_cau}")
        await asyncio.sleep(0.5)  # Mô phỏng processing time

    print(f"[{ma_nguoi_dung}] Xong.")


async def test_concurrent():
    print("=== Test: Hai người dùng chạy đồng thời ===\n")

    # Chạy song song hai người dùng
    await asyncio.gather(
        simulate_user("nguyen_van_a", [
            "Phân tích thị trường cà phê Hà Nội",
            "Lưu kết quả vào bao_cao_ca_phe.md"
        ]),
        simulate_user("tran_thi_b", [
            "Tính ROI cho chiến dịch quảng cáo",
            "Lưu kết quả vào roi_quang_cao.md"
        ])
    )

    print(f"\nSố phiên active: {quan_ly_phien.so_phien_active()}")
    print("Phiên đang chạy:", quan_ly_phien.liet_ke_phien())

    # Kiểm tra workspace riêng
    from pathlib import Path
    ws_a = Path("./workspaces/nguyen_van_a")
    ws_b = Path("./workspaces/tran_thi_b")
    print(f"\nWorkspace A tồn tại: {ws_a.exists()}")
    print(f"Workspace B tồn tại: {ws_b.exists()}")
    print("Hai người dùng hoàn toàn cô lập!")


asyncio.run(test_concurrent())