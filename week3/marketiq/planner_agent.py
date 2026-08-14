from pydantic import BaseModel, Field
from agents import Agent

SO_LUONG_TIM_KIEM = 5

INSTRUCTIONS = f"""Bạn là chuyên gia nghiên cứu thị trường Việt Nam.
Khi nhận được một câu hỏi nghiên cứu, hãy lập kế hoạch tìm kiếm thông tin toàn diện.

Tạo ra đúng {SO_LUONG_TIM_KIEM} từ khoá tìm kiếm để trả lời câu hỏi.

Nguyên tắc tạo từ khoá tốt:
- Đa dạng góc nhìn: quy mô thị trường, xu hướng, công ty cụ thể, thách thức, cơ hội
- Cụ thể hoá cho Việt Nam: thêm "Việt Nam", "TP.HCM", năm hiện tại khi phù hợp
- Tránh quá chung chung: "kinh doanh Việt Nam" → "doanh thu ngành F&B Việt Nam 2025 2026"
- Kết hợp tiếng Việt và tiếng Anh nếu chủ đề có nguồn tiếng Anh phong phú hơn"""


class WebSearchItem(BaseModel):
    reason: str = Field(
        description="Lý do tại sao từ khoá này quan trọng để trả lời câu hỏi nghiên cứu."
    )
    query: str = Field(
        description="Từ khoá cụ thể để tìm kiếm trên internet."
    )


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(
        description="Danh sách các từ khoá cần tìm kiếm để nghiên cứu toàn diện."
    )


planner_agent = Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)