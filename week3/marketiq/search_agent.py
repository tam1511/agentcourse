import os
import asyncio
from tavily import TavilyClient
from agents import Agent, function_tool, ModelSettings

INSTRUCTIONS = (
    "Bạn là trợ lý nghiên cứu thị trường Việt Nam. "
    "Khi được cho một từ khoá tìm kiếm, hãy dùng tool để tìm thông tin. "
    "Tổng hợp thành bản tóm tắt ngắn gọn 2-3 đoạn văn, dưới 300 từ. "
    "Ưu tiên số liệu, thống kê, tên công ty cụ thể. "
    "Không thêm bình luận nào ngoài phần tóm tắt."
)


@function_tool
async def tim_kiem_web(tu_khoa: str) -> str:
    def blocking_call():
        client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
        return client.search(
            query=tu_khoa,
            max_results=5,
            search_depth="basic",
            include_answer=True,
        )

    ket_qua = await asyncio.to_thread(blocking_call)

    output = []
    if ket_qua.get("answer"):
        output.append(f"Tóm tắt nhanh: {ket_qua['answer']}\n")

    for i, item in enumerate(ket_qua["results"], 1):
        output.append(f"[{i}] {item['title']}")
        output.append(f"Nguồn: {item['url']}")
        output.append(f"Nội dung: {item['content'][:400]}")
        output.append("")

    return "\n".join(output)


search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[tim_kiem_web],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)