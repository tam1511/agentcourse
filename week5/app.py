# app.py

import gradio as gr
from pathlib import Path
from agent_core import TroLyAI
from session_manager import quan_ly_phien

# ─── Callbacks ────────────────────────────────────────────────────────

def khoi_tao_phien(yeu_cau_request: gr.Request):
    """Tạo session mới khi người dùng mở app."""
    # Trong demo: dùng IP làm mã user. Production: dùng login system
    ma_user = f"user_{hash(str(yeu_cau_request.client.host)) % 10000:04d}"
    phien = quan_ly_phien.tao_phien_moi(ma_user)

    thu_muc = Path(f"./workspaces/{ma_user}")
    thu_muc.mkdir(parents=True, exist_ok=True)

    agent = TroLyAI(ma_nguoi_dung=ma_user, thu_muc_lam_viec=thu_muc)
    phien.agent = agent

    thong_bao = f"TroLy.AI sẵn sàng phục vụ! Session: {phien.session_id}"
    return phien, thong_bao


def xu_ly_tin_nhan(phien, tin_nhan: str, tieu_chuan: str, lich_su: list):
    """Xử lý tin nhắn người dùng."""
    if not tin_nhan.strip():
        return lich_su, phien

    if not phien or not phien.agent:
        lich_su.append({"role": "assistant", "content": "Session chưa sẵn sàng. Vui lòng refresh."})
        return lich_su, phien

    # Thêm tin nhắn người dùng vào lịch sử
    lich_su.append({"role": "user", "content": tin_nhan})

    ket_qua = phien.agent.xu_ly_yeu_cau(
        tin_nhan=tin_nhan,
        tieu_chuan=tieu_chuan or "Câu trả lời rõ ràng, đầy đủ, và hữu ích cho doanh nghiệp."
    )

    # Câu trả lời chính
    lich_su.append({"role": "assistant", "content": ket_qua["tra_loi"]})

    # Đánh giá từ Evaluator — hiển thị nhẹ hơn
    if ket_qua["danh_gia"]:
        lich_su.append({
            "role": "assistant",
            "content": f"_{ket_qua['danh_gia']}_"
        })

    return lich_su, phien


def dat_lai(phien, yeu_cau_request: gr.Request):
    """Reset — tạo session mới hoàn toàn."""
    if phien and phien.agent:
        phien.agent.don_dep()

    ma_user = f"user_{hash(str(yeu_cau_request.client.host)) % 10000:04d}"
    phien_moi = quan_ly_phien.tao_phien_moi(ma_user)

    thu_muc = Path(f"./workspaces/{ma_user}")
    thu_muc.mkdir(parents=True, exist_ok=True)

    agent_moi = TroLyAI(ma_nguoi_dung=ma_user, thu_muc_lam_viec=thu_muc)
    phien_moi.agent = agent_moi

    thong_bao = f"Đã reset. Session mới: {phien_moi.session_id}"
    return [], "", "", phien_moi, thong_bao


def giai_phong_tai_nguyen(phien):
    """Dọn dẹp khi user đóng tab."""
    if phien and phien.agent:
        phien.agent.don_dep()


# ─── UI ───────────────────────────────────────────────────────────────

with gr.Blocks(
    title="TroLy.AI — Trợ Lý AI Doanh Nghiệp"
) as app:

    phien_state = gr.State(delete_callback=giai_phong_tai_nguyen)

    gr.Markdown("""
    # 🤖 TroLy.AI
    ### Trợ Lý AI Doanh Nghiệp Việt Nam
    Tìm kiếm thông tin · Phân tích số liệu · Viết báo cáo · Nhớ ngữ cảnh
    """)

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="Hội thoại",
                height=450
            )
        with gr.Column(scale=1):
            gr.Markdown("### Hướng dẫn nhanh")
            gr.Markdown("""
**Bạn có thể hỏi:**
- Nghiên cứu thị trường X
- Phân tích số liệu Y
- Viết báo cáo về Z
- Tính ROI cho chiến dịch...
- Lưu kết quả vào file...

**Tools có sẵn:**
- Web Search
- File Manager
- Tính toán
- Lưu báo cáo
            """)
            trang_thai_label = gr.Textbox(
                label="Trạng thái",
                value="Đang khởi tạo...",
                interactive=False
            )

    with gr.Group():
        tin_nhan_input = gr.Textbox(
            label="Yêu cầu của bạn",
            placeholder="Ví dụ: Nghiên cứu thị trường trà sữa tại TP.HCM và lưu báo cáo",
            lines=2
        )
        tieu_chuan_input = gr.Textbox(
            label="Tiêu chuẩn thành công (tùy chọn)",
            placeholder="Ví dụ: Báo cáo phải có số liệu thị trường, 3 đối thủ chính, và đề xuất cụ thể",
            lines=1
        )

    with gr.Row():
        nut_gui = gr.Button("Gửi", variant="primary", scale=3)
        nut_reset = gr.Button("Reset", variant="stop", scale=1)

    # ── Event handlers ──────────────────────────────────────────────
    app.load(
        khoi_tao_phien,
        inputs=[],
        outputs=[phien_state, trang_thai_label]
    )

    nut_gui.click(
        xu_ly_tin_nhan,
        inputs=[phien_state, tin_nhan_input, tieu_chuan_input, chatbot],
        outputs=[chatbot, phien_state]
    ).then(
        lambda: "",
        outputs=[tin_nhan_input]
    )

    tin_nhan_input.submit(
        xu_ly_tin_nhan,
        inputs=[phien_state, tin_nhan_input, tieu_chuan_input, chatbot],
        outputs=[chatbot, phien_state]
    ).then(
        lambda: "",
        outputs=[tin_nhan_input]
    )

    nut_reset.click(
        dat_lai,
        inputs=[phien_state],
        outputs=[chatbot, tin_nhan_input, tieu_chuan_input, phien_state, trang_thai_label]
    )


if __name__ == "__main__":
    app.launch(
    inbrowser=True,
    server_name="0.0.0.0",
    server_port=7860,
    theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate")
)