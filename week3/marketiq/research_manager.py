import asyncio
from agents import Runner, trace, gen_trace_id
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from search_agent import search_agent
from writer_agent import ReportData, writer_agent
from email_agent import email_agent

class ResearchManager:
    async def run(self, query: str):
        trace_id = gen_trace_id() 

        with trace("MarketIQ Research", trace_id=trace_id):
            trace_url = f"https://platform.openai.com/logs/trace?trace_id={trace_id}"
            yield f"Xem trace chi tiết {trace_url}\n\n"

            search_plan = await self.lap_ke_hoach(query)

            search_results = await self.tim_kiem_song_song(search_plan)

            report = await self.viet_bao_cao(query, search_results)

            await self.gui_email(report)
            yield "Email đã được gửi\n"

            yield report.markdown_report

            if report.follow_up_questions:
                follow_up = "Gợi ý nghiên cứu tiếp theo\n"
                for i, q in enumerate(report.follow_up_questions, 1):
                    follow_up += f"\n{i}. {q}"
                yield follow_up

    async def lap_ke_hoach(self, query: str) -> WebSearchPlan:
        result = await Runner.run(planner_agent, f"Câu hỏi nghiên cứu: {query}")
        return result.final_output_as(WebSearchPlan)

    async def tim_kiem_song_song(self, search_plan: WebSearchPlan) -> list[str]:
        print(f"Bắt đầu {len(search_plan.searches)} tìm kiếm song song..")

        coroutines = [
            self.thuc_hien_tim_kiem(item)
            for item in search_plan.searches
        ]
        raw_results = await asyncio.gather(*coroutines, return_exceptions=True)

        ket_qua = []
        for i, result in enumerate(raw_results):
            if isinstance(result, Exception):
                print(f"Tìm kiếm {i+1} thất bại: {result}")
            elif result is not None:
                ket_qua.append(result)

        print(f"Hoàn thành {len(ket_qua)}/{len(search_plan.searches)} tìm kiếm")
        return ket_qua

    async def thuc_hien_tim_kiem(self, item: WebSearchItem) -> str | None:
        prompt = f"Từ khoá: {item.query}\nMục đích tìm kiếm: {item.reason}"
        try:
            result = await Runner.run(search_agent, prompt)
            return str(result.final_output)
        except Exception as e:
            print(f"Lỗi tìm kiếm '{item.query}': {e}")
            return None

    async def viet_bao_cao(self, query: str, search_results: list[str]) -> ReportData:
        noi_dung = (
            f"Câu hỏi nghiên cứu: {query}\n\n"
            f"Kết quả tìm kiếm:\n{'n'*50}\n"
            + "\n\n".join(
                f"[Nguồn {i+1}\n{ket_qua}]"
                for i, ket_qua in enumerate(search_results)
            )
        )
        result = await Runner.run(writer_agent, noi_dung)
        return result.final_output_as(ReportData)

    async def gui_email(self, report: ReportData) -> None:
        await Runner.run(email_agent, report.markdown_report)
        print("Email đã được gửi")

    
