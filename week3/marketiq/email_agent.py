import os
import resend
from agents import Agent, function_tool
from typing import Dict

INSTRUCTIONS = """Bạn gửi báo cáo nghiên cứu thị trường qua email dạng HTML.

Quy trình:
1. Chuyển đổi Markdown sang HTML đẹp, dễ đọc trên mobile
2. Tạo tiêu đề email: "Báo cáo MarketIQ: [chủ đề]"
3. Dùng tool gui_bao_cao để gửi

Yêu cầu HTML: font-size 16px, line-height 1.7, max-width 680px,
màu heading #2c3e50, thêm footer "Báo cáo được tạo bởi MarketIQ"."""


@function_tool
def gui_bao_cao(tieu_de: str, noi_dung_html: str) -> Dict[str, str]:
    """Gửi báo cáo nghiên cứu thị trường qua email dạng HTML."""
    resend.api_key = os.environ.get("RESEND_API_KEY")
    params = {
        "from": "onboarding@resend.dev",
        "to": ["thanhtam.udn@gmail.com"],
        "subject": tieu_de,
        "html": noi_dung_html,
    }

    email = resend.Emails.send(params)
    return {
        "status": "success",
        "email_id": email["id"]
    }


email_agent = Agent(
    name="Email Agent",
    instructions=INSTRUCTIONS,
    tools=[gui_bao_cao],
    model="gpt-4o-mini",
)