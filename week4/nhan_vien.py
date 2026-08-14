"""
nhan_vien.py — Module NhanVien: Agent CSKH tự động cho Shop Online
"""
import asyncio
from contextlib import AsyncExitStack
from datetime import datetime

from dotenv import load_dotenv
from agents import Agent, Runner, Tool, trace

from agents.mcp import MCPServerStdio
from mcp_params_shop import nhan_vien_mcp_server_params, nghien_cuu_mcp_server_params
from templates_shop import (
    nghien_cuu_instructions, cong_cu_nghien_cuu,
    nhan_vien_instructions,
    nhiem_vu_xu_ly_don, nhiem_vu_phan_tich_doanh_thu, nhiem_vu_tai_can_bang,
)

load_dotenv(override=True)

DEFAULT_MODEL = "gpt-4o-mini"


class NhanVien:
    """
    Đại diện cho một nhân viên CSKH tự động với researcher agent hỗ trợ.

    Mỗi NhanVien có:
    - Tên và chức vụ riêng
    - Bộ MCP servers cho công việc nghiệp vụ
    - Researcher sub-agent có memory graph riêng
    - Khả năng luân phiên giữa 3 nhiệm vụ: xử lý đơn, phân tích, tái cân bằng
    """

    def __init__(
        self,
        ten: str,
        chuc_vu: str = "Nhân viên CSKH",
        model: str = DEFAULT_MODEL,
    ):
        self.ten      = ten
        self.chuc_vu  = chuc_vu
        self.model    = model
        self._vu_hien_tai = 0   # Luân phiên qua 3 nhiệm vụ

    async def _tao_researcher_tool(self, researcher_servers: list) -> Tool:
        """Tạo researcher agent và convert thành tool cho nhân viên dùng."""
        researcher = Agent(
            name=f"Researcher-{self.ten}",
            instructions=nghien_cuu_instructions(),
            model=self.model,
            mcp_servers=researcher_servers,
        )
        return researcher.as_tool(
            tool_name="researcher",
            tool_description=cong_cu_nghien_cuu(),
        )

    async def _chon_nhiem_vu(self) -> str:
        """Luân phiên qua 3 nhiệm vụ theo vòng tròn."""
        danh_sach_don = (
            f"- Xem và xác nhận đơn hàng mới\n"
            f"- Cập nhật trạng thái đơn đang chờ\n"
            f"- Kiểm tra tỷ giá để định giá sản phẩm nhập khẩu"
        )
        lich_su = (
            f"Đã xử lý đơn hàng và phân tích doanh thu trong các ca trước. "
            f"Hiện cần rà soát chiến lược tổng thể."
        )

        nhiem_vu = [
            nhiem_vu_xu_ly_don(self.ten, danh_sach_don),
            nhiem_vu_phan_tich_doanh_thu(self.ten),
            nhiem_vu_tai_can_bang(self.ten, lich_su),
        ]
        ten_nhiem_vu = ["Xử lý đơn hàng", "Phân tích doanh thu", "Tái cân bằng chiến lược"]

        index = self._vu_hien_tai % 3
        print(f"\n[{self.ten}] Nhiệm vụ: {ten_nhiem_vu[index]}")
        self._vu_hien_tai += 1
        return nhiem_vu[index]

    async def run(self) -> str:
        """
        Chạy nhân viên với AsyncExitStack để quản lý nhiều context managers gọn gàng.

        Pattern này tương đương với việc viết:
            async with MCPServerStdio(p1) as s1:
                async with MCPServerStdio(p2) as s2:
                    async with MCPServerStdio(p3) as s3:
                        ...
        Nhưng không bị nested sâu khi có nhiều servers.
        """
        nv_params   = nhan_vien_mcp_server_params
        nc_params   = nghien_cuu_mcp_server_params(self.ten)
        tat_ca_params = nv_params + nc_params

        async with AsyncExitStack() as stack:
            # Khởi động TẤT CẢ servers cùng lúc — gọn hơn nhiều nested with
            tat_ca_servers = [
                await stack.enter_async_context(
                    MCPServerStdio(params=p, client_session_timeout_seconds=60)
                )
                for p in tat_ca_params
            ]

            nv_servers = tat_ca_servers[:len(nv_params)]
            nc_servers = tat_ca_servers[len(nv_params):]

            # Tạo researcher tool
            researcher_tool = await self._tao_researcher_tool(nc_servers)

            # Tạo nhân viên agent
            agent = Agent(
                name=self.ten,
                instructions=nhan_vien_instructions(self.ten, self.chuc_vu),
                tools=[researcher_tool],
                mcp_servers=nv_servers,
                model=self.model,
            )

            # Chọn nhiệm vụ và chạy
            nhiem_vu = await self._chon_nhiem_vu()
            trace_id = f"{self.ten.lower()}-{datetime.now().strftime('%H%M%S')}"

            with trace(trace_id):
                result = await Runner.run(agent, nhiem_vu, max_turns=45)

            print(f"\n[{self.ten}] Hoàn thành:\n{result.final_output[:500]}...")
            return result.final_output


# ── Convenience function: chạy nhiều nhân viên song song ─────────────────

async def chay_tat_ca(danh_sach: list[NhanVien]) -> list[str]:
    """Chạy nhiều nhân viên song song với asyncio.gather."""
    return await asyncio.gather(*[nv.run() for nv in danh_sach])