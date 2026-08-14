from mcp.server.fastmcp import FastMCP
from dulieu_vn import (
    lay_ty_gia, so_sanh_ty_gia,
    lay_gia_vang, tat_ca_gia_vang,
    tim_bat_dong_san, thong_ke_thi_truong, tinh_roi_cho_thue
)
from typing import Optional

mcp = FastMCP("du_lieu_tai_chinh_vn")


# ── Tỷ giá ──────────────────────────────────────────────────────────────

@mcp.tool()
async def ty_gia_ngoai_te(loai_tien: str) -> dict:
    """Lấy tỷ giá hối đoái của một loại ngoại tệ so với VNĐ từ Vietcombank.
    Dùng khi cần biết tỷ giá mua/bán của USD, EUR, JPY, CNY, KRW, SGD và các ngoại tệ khác.

    Args:
        loai_tien: Mã ngoại tệ quốc tế — ví dụ: USD, EUR, JPY, CNY, SGD, KRW
    """
    return lay_ty_gia(loai_tien)


@mcp.tool()
async def so_sanh_nhieu_ngoai_te(danh_sach_tien: str) -> list:
    """So sánh tỷ giá của nhiều loại ngoại tệ cùng lúc.
    Dùng khi cần so sánh tỷ giá nhiều đồng tiền để hỗ trợ quyết định đầu tư hoặc giao dịch ngoại thương.

    Args:
        danh_sach_tien: Các mã ngoại tệ phân cách bằng dấu phẩy — ví dụ: "USD,EUR,JPY"
    """
    tien_list = [t.strip() for t in danh_sach_tien.split(",")]
    return so_sanh_ty_gia(tien_list)


# ── Giá vàng ────────────────────────────────────────────────────────────

@mcp.tool()
async def gia_vang_hom_nay(loai_vang: Optional[str] = None) -> dict:
    """Lấy giá vàng hiện tại từ SJC.
    Dùng khi cần biết giá vàng mua/bán để tư vấn đầu tư hoặc so sánh kênh đầu tư.

    Args:
        loai_vang: Loại vàng muốn xem — ví dụ: SJC, RING, PNJ, DOJI.
                   Để trống sẽ trả về vàng SJC 1L chính.
    """
    return lay_gia_vang(loai_vang)


@mcp.tool()
async def tat_ca_loai_vang() -> list:
    """Lấy giá vàng tất cả các loại (SJC miếng, nhẫn, PNJ, DOJI...).
    Dùng khi cần bảng so sánh giá vàng toàn thị trường.
    """
    return tat_ca_gia_vang()


# ── Bất động sản ────────────────────────────────────────────────────────

@mcp.tool()
async def tim_nha_dat(khu_vuc: Optional[str] = None,
                      loai_bat_dong_san: Optional[str] = None,
                      gia_toi_da_ty: Optional[float] = None) -> list:
    """Tìm kiếm bất động sản theo khu vực, loại, và giới hạn ngân sách.
    Dùng khi cần tra cứu giá bất động sản thị trường tại HCM hoặc Hà Nội.

    Args:
        khu_vuc: Khu vực tìm kiếm — ví dụ: "Quận 7", "Bình Thạnh", "Cầu Giấy", "Đống Đa"
        loai_bat_dong_san: chung_cu hoặc nha_pho (tùy chọn)
        gia_toi_da_ty: Giá tối đa tính bằng tỷ VNĐ — ví dụ: 4.0 cho tối đa 4 tỷ (tùy chọn)
    """
    return tim_bat_dong_san( khu_vuc or "", gia_toi_da_ty)


@mcp.tool()
async def thong_ke_gia_thi_truong(khu_vuc: Optional[str] = None) -> list:
    """Thống kê giá bất động sản trung bình, min, max theo từng khu vực.
    Dùng khi cần phân tích và so sánh mặt bằng giá giữa các quận/huyện.

    Args:
        khu_vuc: Lọc theo khu vực cụ thể — "HCM" cho TP.HCM, "HN" cho Hà Nội (tùy chọn)
    """
    return thong_ke_thi_truong(khu_vuc)


@mcp.tool()
async def tinh_roi_dau_tu(gia_mua_ty: float,
                           dien_tich_m2: float,
                           khu_vuc: str) -> dict:
    """Tính toán hiệu quả đầu tư cho thuê bất động sản (gross yield và thời gian hoàn vốn).
    Dùng khi cần đánh giá tính hiệu quả của một khoản đầu tư BĐS cụ thể.

    Args:
        gia_mua_ty: Giá mua bất động sản tính bằng tỷ VNĐ — ví dụ: 3.8
        dien_tich_m2: Diện tích căn hộ/nhà tính bằng m² — ví dụ: 68
        khu_vuc: Khu vực của bất động sản — ví dụ: "Quận 7 HCM", "Cầu Giấy HN"
    """
    return tinh_roi_cho_thue(gia_mua_ty, dien_tich_m2, khu_vuc)


# ── Resource: báo cáo thị trường tổng hợp ───────────────────────────────

@mcp.resource("taichinh://thi-truong/{thanh_pho}")
async def bao_cao_thi_truong(thanh_pho: str) -> str:
    """Báo cáo tổng hợp thị trường tài chính và BĐS theo thành phố."""
    from dulieu_vn import _ngay_hom_nay
    stats = thong_ke_thi_truong(khu_vuc=thanh_pho[:2].upper())
    vang = lay_gia_vang()
    usd  = lay_ty_gia("USD")

    lines = [
        f"=== Báo Cáo Thị Trường — {thanh_pho.upper()} ===",
        f"Ngày: {_ngay_hom_nay()}\n",
        "── Tỷ giá & Vàng ──────────────────────────────────",
        f"USD/VNĐ: mua {usd['mua_chuyen_khoan']} | bán {usd['ban']} (Vietcombank)",
        f"Vàng SJC: mua {vang['mua']} | bán {vang['ban']}\n",
        "── Bất động sản ────────────────────────────────────",
    ]
    for s in stats:
        lines.append(
            f"{s['khu_vuc']} ({s['loai']}): TB {s['gia_trung_binh']} "
            f"({s['so_tin_rao']} tin)"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")