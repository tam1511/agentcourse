"""
MCP Client thủ công cho server quản lý đơn hàng.
Mục đích: hiểu cơ chế bên dưới trước khi dùng SDK.
"""
import mcp
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from agents import FunctionTool
import json

# Tham số để spawn server — giống hệt params trong MCPServerStdio
params = StdioServerParameters(
    command="python",
    args=["donhang_server.py"],
    env=None
)

async def liet_ke_tools():
    """Lấy danh sách tools từ server."""
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.list_tools()
            return result.tools

async def goi_tool(ten_tool: str, tham_so: dict):
    """Gọi một tool cụ thể với tham số cho trước."""
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool(ten_tool, tham_so)
            return result

async def doc_resource_khach(ten_khach: str) -> str:
    """Đọc resource lịch sử đơn hàng của một khách hàng."""
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.read_resource(f"donhang://shop/{ten_khach}")
            return result.contents[0].text

async def lay_tools_openai():
    """Chuyển đổi tools MCP sang format OpenAI Agents SDK."""
    openai_tools = []
    for tool in await liet_ke_tools():
        schema = {**tool.inputSchema, "additionalProperties": False}
        openai_tool = FunctionTool(
            name=tool.name,
            description=tool.description,
            params_json_schema=schema,
            on_invoke_tool=lambda ctx, args, tn=tool.name: goi_tool(tn, json.loads(args))
        )
        openai_tools.append(openai_tool)
    return openai_tools