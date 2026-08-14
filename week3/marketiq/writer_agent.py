from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "Bạn là chuyên gia phân tích kinh doanh và nghiên cứu thị trường Việt Nam. "
    "Bạn sẽ được cung cấp câu hỏi nghiên cứu và kết quả tìm kiếm từ trợ lý nghiên cứu.\n"
    "Trước tiên lập outline cấu trúc báo cáo, sau đó viết báo cáo đầy đủ.\n"
    "Cấu trúc: Tổng quan → Phân tích chi tiết → Cơ hội → Thách thức → Khuyến nghị.\n"
    "Yêu cầu: định dạng Markdown, có số liệu và case study cụ thể từ Việt Nam, "
    "độ dài tối thiểu 1000 từ. Ngôn ngữ: tiếng Việt, chuyên nghiệp nhưng dễ hiểu."
)


class ReportData(BaseModel):
    short_summary: str = Field(
        description="Tóm tắt ngắn gọn 2-3 câu nêu bật phát hiện quan trọng nhất."
    )
    markdown_report: str = Field(
        description="Báo cáo nghiên cứu đầy đủ định dạng Markdown."
    )
    follow_up_questions: list[str] = Field(
        description="3-5 câu hỏi nghiên cứu tiếp theo nên tìm hiểu thêm."
    )


writer_agent = Agent(
    name="Writer Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)
