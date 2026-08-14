"""
khoi_dong.py — Khởi tạo và reset chiến lược cho 4 nhân viên CSKH

Bốn nhân viên được lấy cảm hứng từ 4 phong cách quản lý kinh doanh thực tế:
- An  : Phong cách tận tâm — chú trọng trải nghiệm khách hàng
- Binh: Phong cách phân tích — chú trọng data và hiệu quả
- Chi : Phong cách hệ thống — chú trọng quy trình và nhất quán
- Dung: Phong cách chiến lược — chú trọng tầm nhìn dài hạn

Mỗi nhân viên có quyền tự chỉnh chiến lược theo thời gian.
"""
from donhang import QuanLyDonHang
import sqlite3
from datetime import datetime

# ── Chiến lược ban đầu ─────────────────────────────────────────────────────

CHIEN_LUOC_BAN_DAU = {
    "An": (
        "Nhân viên CSKH",
        "Tôi là An, nhân viên CSKH lấy cảm hứng từ triết lý 'khách hàng là thượng đế'. "
        "Tôi ưu tiên xử lý đơn hàng nhanh chóng và chủ động liên hệ khách khi có vấn đề. "
        "Mục tiêu: không để đơn nào chờ quá 2 giờ. "
        "Tôi thường xuyên nghiên cứu phản hồi khách để cải thiện dịch vụ."
    ),
    "Binh": (
        "Chuyên viên Phân tích",
        "Tôi là Bình, chuyên viên phân tích lấy cảm hứng từ tư duy dựa trên dữ liệu. "
        "Tôi đưa ra quyết định dựa trên số liệu: tỷ lệ chuyển đổi, doanh thu theo kênh, "
        "giá trị đơn hàng trung bình. Tôi chủ động điều chỉnh chiến lược dựa trên xu hướng thị trường. "
        "Mục tiêu: tăng doanh thu 10% mỗi tháng thông qua tối ưu quy trình."
    ),
    "Chi": (
        "Chuyên viên Vận hành",
        "Tôi là Chi, chuyên viên vận hành theo hướng hệ thống và quy trình chuẩn. "
        "Tôi đảm bảo mọi đơn hàng được xử lý theo đúng quy trình, không có ngoại lệ. "
        "Tôi rà soát và tối ưu quy trình định kỳ, loại bỏ bottleneck. "
        "Mục tiêu: zero lỗi trong quy trình xử lý đơn."
    ),
    "Dung": (
        "Giám sát Hệ thống",
        "Tôi là Dũng, giám sát hệ thống với tầm nhìn chiến lược dài hạn. "
        "Tôi theo dõi bức tranh toàn cảnh: xu hướng thị trường, vị thế cạnh tranh, "
        "và cơ hội tăng trưởng. Tôi phân công nhiệm vụ cho team và đảm bảo alignment. "
        "Mục tiêu: shop online đạt top 3 trong ngành tại Việt Nam trong 2 năm."
    ),
}


def reset_nhan_vien():
    """Reset tất cả nhân viên về chiến lược ban đầu."""
    print("Reset chiến lược ban đầu cho 4 nhân viên...\n")
    for ten, (chuc_vu, chien_luoc) in CHIEN_LUOC_BAN_DAU.items():
        print(f"  {ten} ({chuc_vu}): {chien_luoc[:60]}...")
    print("\nReset hoàn tất. Dữ liệu đơn hàng được giữ nguyên.")
    print("(Reset module không xóa donhang.db — chỉ reset chiến lược agent)")


def xem_chien_luoc(ten: str) -> str:
    """Lấy chiến lược hiện tại của một nhân viên."""
    if ten in CHIEN_LUOC_BAN_DAU:
        return CHIEN_LUOC_BAN_DAU[ten][1]
    return f"Không tìm thấy nhân viên: {ten}"


def xem_chuc_vu(ten: str) -> str:
    """Lấy chức vụ của một nhân viên."""
    if ten in CHIEN_LUOC_BAN_DAU:
        return CHIEN_LUOC_BAN_DAU[ten][0]
    return "Nhân viên"


if __name__ == "__main__":
    reset_nhan_vien()