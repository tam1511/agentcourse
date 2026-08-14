"""
app_shop.py — Giao diện theo dõi hoạt động nhân viên CSKH
Gradio app hiển thị log thời gian thực từ database.

Cách chạy (terminal riêng):
    python app_shop.py
"""
import gradio as gr
import sqlite3
from datetime import datetime
from pathlib import Path
from database_shop import doc_log, doc_log_tat_ca, DB_PATH
from donhang import QuanLyDonHang

TEN_NHAN_VIEN = ["An", "Binh", "Chi", "Dung"]

ICON_LOAI = {
    "trace": "🔄", "tool": "🔧", "agent": "🤖",
    "hoan_thanh": "✓",  "bao_cao": "📊",
    "canh_bao": "⚠", "loi": "✗", "span": "⚙",
}


def _format_log(rows: list) -> str:
    if not rows:
        return "_Chưa có hoạt động_"
    lines = []
    for r in rows:
        icon = ICON_LOAI.get(r.get("loai", ""), "•")
        tao_luc = r.get("tao_luc", "")[:16].replace("T", " ")
        noi_dung = r.get("noi_dung", "")[:120]
        lines.append(f"`{tao_luc}` {icon} {noi_dung}")
    return "\n\n".join(lines)


def _doanh_thu_hom_nay() -> str:
    dt = QuanLyDonHang.doanh_thu()
    return (
        f"**{dt['so_don_hang']} đơn hàng**  \n"
        f"Tổng: **{dt['tong_doanh_thu']:,.0f} VNĐ**"
    )


def _don_hang_theo_trang_thai() -> str:
    tat_ca = QuanLyDonHang.danh_sach_don()
    from collections import Counter
    ts = Counter(d["trang_thai"] for d in tat_ca)
    nhans = {
        "cho_xac_nhan": "⏳ Chờ xác nhận",
        "dang_xu_ly":   "⚙ Đang xử lý",
        "dang_giao":    "🚚 Đang giao",
        "da_giao":      "✓ Đã giao",
        "da_huy":       "✗ Đã hủy",
    }
    lines = []
    for k, label in nhans.items():
        if k in ts:
            lines.append(f"{label}: **{ts[k]}**")
    return "\n\n".join(lines) if lines else "_Chưa có đơn hàng_"


def _log_nhan_vien(ten: str) -> str:
    rows = doc_log(ten, gioi_han=15)
    return _format_log(rows)


def _log_tat_ca() -> str:
    rows = doc_log_tat_ca(gioi_han=30)
    lines = []
    for r in rows:
        icon = ICON_LOAI.get(r.get("loai", ""), "•")
        tao_luc = r.get("tao_luc", "")[:16].replace("T", " ")
        nv = r.get("ten_nv", "?")
        noi_dung = r.get("noi_dung", "")[:100]
        lines.append(f"`{tao_luc}` **{nv}** {icon} {noi_dung}")
    return "\n\n".join(lines) if lines else "_Chưa có hoạt động_"


def lam_moi():
    """Refresh tất cả panels — gọi khi nhấn nút hoặc auto-refresh."""
    return (
        _doanh_thu_hom_nay(),
        _don_hang_theo_trang_thai(),
        _log_nhan_vien("An"),
        _log_nhan_vien("Binh"),
        _log_nhan_vien("Chi"),
        _log_nhan_vien("Dung"),
        _log_tat_ca(),
    )


# ── Build Gradio UI ───────────────────────────────────────────────────────
with gr.Blocks(title="TrendVN — Sàn CSKH Tự Động") as app:
    gr.Markdown("# 🛒 TrendVN — Sàn Vận Hành CSKH Tự Động")
    gr.Markdown("Theo dõi hoạt động 4 nhân viên AI đang làm việc song song.")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Doanh thu")
            doanh_thu_box = gr.Markdown(_doanh_thu_hom_nay())

        with gr.Column(scale=1):
            gr.Markdown("### 📦 Đơn hàng")
            don_hang_box = gr.Markdown(_don_hang_theo_trang_thai())

        with gr.Column(scale=1):
            btn_refresh = gr.Button("🔄 Làm mới", variant="primary")
            gr.Markdown(f"*Cập nhật lúc:*  \n`{datetime.now().strftime('%H:%M:%S')}`")

    gr.Markdown("---")
    gr.Markdown("## 👥 Hoạt động từng nhân viên")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### An — CSKH")
            log_an = gr.Markdown(_log_nhan_vien("An"))

        with gr.Column():
            gr.Markdown("### Bình — Phân tích")
            log_binh = gr.Markdown(_log_nhan_vien("Binh"))

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Chi — Vận hành")
            log_chi = gr.Markdown(_log_nhan_vien("Chi"))

        with gr.Column():
            gr.Markdown("### Dũng — Giám sát")
            log_dung = gr.Markdown(_log_nhan_vien("Dung"))

    gr.Markdown("---")
    gr.Markdown("## 🌐 Log toàn hệ thống")
    log_all = gr.Markdown(_log_tat_ca())

    # Kết nối nút refresh
    btn_refresh.click(
        fn=lam_moi,
        outputs=[doanh_thu_box, don_hang_box, log_an, log_binh, log_chi, log_dung, log_all]
    )


if __name__ == "__main__":
    print("Khởi động Gradio UI tại http://localhost:7860")
    print("Nhấn Ctrl+C để dừng")
    app.launch(share=False)