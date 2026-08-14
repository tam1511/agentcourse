import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

PLACEHOLDER_QUERIES = [
    "Cơ hội và thách thức khi mở chuỗi trà sữa tại Việt Nam năm 2026",
    "So sánh Shopee vs TikTok Shop — seller nên tập trung sàn nào?",
    "Xu hướng và tiềm năng ngành Edtech tại Việt Nam 2026",
    "Thị trường SaaS B2B Việt Nam — cơ hội cho startup nội địa",
]


async def chay_nghien_cuu(query: str):
    """Callback cho Gradio — async generator yield từng chunk."""
    if not query or not query.strip():
        yield "Vui lòng nhập câu hỏi nghiên cứu trước khi bấm Run."
        return

    noi_dung_hien_tai = ""
    try:
        async for chunk in ResearchManager().run(query.strip()):
            # str() đảm bảo an toàn nếu chunk không phải string
            noi_dung_hien_tai += str(chunk) + "\n"
            yield noi_dung_hien_tai
    except Exception as e:
        yield f"{noi_dung_hien_tai}\n\n Lỗi: {str(e)}"


# ─── Giao diện Gradio ─────────────────────────────────────────────────────────

with gr.Blocks(title="MarketIQ — AI Research Agent") as ui:

    gr.Markdown("""
# MarketIQ — AI Research Agent
**Nghiên cứu thị trường chuyên sâu cho doanh nghiệp Việt Nam**

Nhập câu hỏi nghiên cứu → AI tự động lập kế hoạch, tìm kiếm và tổng hợp báo cáo.
Báo cáo sẽ được gửi qua email sau khi hoàn thành.
""")

    with gr.Row():
        with gr.Column(scale=3):
            query_box = gr.Textbox(
                label="Câu hỏi nghiên cứu",
                placeholder="Ví dụ: Cơ hội và thách thức khi mở chuỗi trà sữa tại Việt Nam 2026",
                lines=3,
            )
        with gr.Column(scale=1):
            run_button = gr.Button("Bắt đầu nghiên cứu", variant="primary", size="lg")

    gr.Examples(
        examples=PLACEHOLDER_QUERIES,
        inputs=query_box,
        label="Ví dụ câu hỏi — click để điền tự động",
    )

    report_output = gr.Markdown(
        label="Báo cáo nghiên cứu",
        value="*Kết quả sẽ hiển thị tại đây...*",
    )

    gr.Markdown("---\n*MarketIQ sử dụng OpenAI GPT-4o-mini + Tavily Search. Chi phí mỗi báo cáo ≈ $0.02.*")

    # Kết nối sự kiện
    run_button.click(fn=chay_nghien_cuu, inputs=query_box, outputs=report_output)
    query_box.submit(fn=chay_nghien_cuu, inputs=query_box, outputs=report_output)


if __name__ == "__main__":
    ui.queue()
    ui.launch(server_name="0.0.0.0", server_port=7860)