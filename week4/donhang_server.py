# donhang_server.py
from mcp.server.fastmcp import FastMCP
from donhang import QuanLyDonHang
from typing import Optional

mcp = FastMCP("quan_ly_don_hang")


@mcp.tool()
async def tao_don_hang(khach_hang: str, san_pham: str,
                       so_luong: int, don_gia: float,
                       ghi_chu: str = "") -> dict:
    """Tạo một đơn hàng mới cho khách hàng.

    Args:
        khach_hang: Tên khách hàng đặt hàng
        san_pham: Tên sản phẩm khách hàng muốn mua
        so_luong: Số lượng sản phẩm
        don_gia: Đơn giá mỗi sản phẩm tính bằng VNĐ
        ghi_chu: Ghi chú — thời gian giao, địa chỉ đặc biệt (tùy chọn)
    """
    return QuanLyDonHang.tao_don(khach_hang, san_pham, so_luong, don_gia, ghi_chu)


@mcp.tool()
async def cap_nhat_trang_thai_don(ma_don: str, trang_thai: str) -> dict:
    """Cập nhật trạng thái xử lý của một đơn hàng.

    Args:
        ma_don: Mã đơn hàng cần cập nhật (ví dụ: DH20250101120000)
        trang_thai: Trạng thái mới — chọn đúng một trong:
                    cho_xac_nhan | dang_xu_ly | dang_giao | da_giao | da_huy
    """
    return QuanLyDonHang.cap_nhat_trang_thai(ma_don, trang_thai)


@mcp.tool()
async def xem_chi_tiet_don(ma_don: str) -> dict:
    """Xem thông tin chi tiết của một đơn hàng theo mã đơn.

    Args:
        ma_don: Mã đơn hàng cần xem (ví dụ: DH20250101120000)
    """
    return QuanLyDonHang.xem_don(ma_don)


@mcp.tool()
async def danh_sach_don_hang(khach_hang: Optional[str] = None,
                              trang_thai: Optional[str] = None) -> list:
    """Lấy danh sách đơn hàng, có thể lọc theo khách hàng hoặc trạng thái.

    Args:
        khach_hang: Tên hoặc một phần tên khách hàng để lọc (tùy chọn)
        trang_thai: Lọc theo trạng thái (tùy chọn):
                    cho_xac_nhan / dang_xu_ly / dang_giao / da_giao / da_huy
    """
    return QuanLyDonHang.danh_sach_don(khach_hang, trang_thai)


@mcp.tool()
async def bao_cao_doanh_thu(ngay_tu: Optional[str] = None,
                             ngay_den: Optional[str] = None) -> dict:
    """Tính tổng doanh thu và số đơn hàng trong khoảng thời gian.

    Args:
        ngay_tu: Ngày bắt đầu định dạng YYYY-MM-DD (tùy chọn)
        ngay_den: Ngày kết thúc định dạng YYYY-MM-DD (tùy chọn)
    """
    return QuanLyDonHang.doanh_thu(ngay_tu, ngay_den)


@mcp.resource("donhang://shop/{ten_khach}")
async def xem_lich_su_khach(ten_khach: str) -> str:
    """Xem toàn bộ lịch sử đặt hàng của một khách hàng dưới dạng báo cáo."""
    orders = QuanLyDonHang.danh_sach_don(khach_hang=ten_khach)
    if not orders:
        return f"Không tìm thấy đơn hàng nào của khách: {ten_khach}"
    total = sum(
        o["so_luong"] * o["don_gia"]
        for o in orders if o["trang_thai"] != "da_huy"
    )
    lines = [f"=== Lịch sử đặt hàng: {ten_khach} ===\n"]
    for o in orders:
        lines.append(
            f"[{o['ma_don']}] {o['san_pham']} x{o['so_luong']} — "
            f"{o['don_gia']:,.0f}đ — {o['trang_thai']}"
        )
    lines.append(f"\nTổng chi tiêu: {total:,.0f} VNĐ | Số đơn: {len(orders)}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")