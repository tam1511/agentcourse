"""
mcp_params_shop.py — Cấu hình MCP Servers cho hệ thống CSKH Shop Online
Tách biệt config khỏi logic — dễ thay đổi server mà không sửa code chính.
"""
import os, subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)

# ── Tìm npm global root (cross-platform) ─────────────────────────────────
NPM_ROOT    = subprocess.check_output(["npm", "root", "-g"]).decode().strip()
MEM_PATH    = os.path.join(NPM_ROOT, "@modelcontextprotocol", "server-memory",    "dist", "index.js")
FS_PATH     = os.path.join(NPM_ROOT, "@modelcontextprotocol", "server-filesystem", "dist", "index.js")
TAVILY_PATH = os.path.join(NPM_ROOT, "tavily-mcp", "build", "index.js")

# ── Thư mục dự án (chứa các file .py của server) ─────────────────────────
PROJECT_DIR = str(Path(__file__).parent.resolve())
SANDBOX     = os.path.join(PROJECT_DIR, "sandbox")
os.makedirs(SANDBOX, exist_ok=True)
os.makedirs(os.path.join(PROJECT_DIR, "memory"), exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════
# MCP Servers cho NHÂN VIÊN CSKH
# Loại 1 (local): Quản lý đơn hàng + Thông báo + Filesystem
# ═══════════════════════════════════════════════════════════════════════════

nhan_vien_mcp_server_params = [
    # Server đơn hàng — tự build (Loại 2: local + SQLite)
    {
        "type": "stdio",
        "command": "/Users/macos/miniconda3/envs/agents-env/bin/python",
        "args":    [os.path.join(PROJECT_DIR, "donhang_server.py")],
    },
    # Server dữ liệu tài chính VN — tự build (Loại 2: local + Vietcombank/SJC APIs)
    {
        "type": "stdio",
        "command": "/Users/macos/miniconda3/envs/agents-env/bin/python",
        "args":    [os.path.join(PROJECT_DIR, "dulieu_vn_server.py")],
    },
    # Server thông báo — tự build (Loại 1: local SQLite log)
    {
        "type": "stdio",
        "command": "/Users/macos/miniconda3/envs/agents-env/bin/python",
        "args":    [os.path.join(PROJECT_DIR, "thong_bao_server.py")],
    },
    # Filesystem — lưu báo cáo ra file (Loại 1: local)
    {
        "type": "stdio",
        "command": "/Users/macos/.nvm/versions/node/v20.20.0/bin/node",
        "args": [FS_PATH, SANDBOX],
    },
]


# ═══════════════════════════════════════════════════════════════════════════
# MCP Servers cho NHÂN VIÊN NGHIÊN CỨU
# Loại 3 (remote API): Tavily Search
# Loại 1 (local): Memory knowledge graph — riêng cho từng nhân viên
# ═══════════════════════════════════════════════════════════════════════════

def nghien_cuu_mcp_server_params(ten_nhan_vien: str) -> list:
    """Mỗi nhân viên có memory graph riêng biệt — tên file dựa trên tên nhân viên."""
    mem_db = os.path.join(PROJECT_DIR, "memory", f"{ten_nhan_vien.lower()}.db")
    return [
        # Tavily Search — tìm kiếm web (Loại 3: remote API)
        {
            "type": "stdio",
            "command": "/Users/macos/.nvm/versions/node/v20.20.0/bin/node",
            "args":    [TAVILY_PATH],
            "env":     {**os.environ, "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY", "")},
        },
        # Memory — knowledge graph riêng cho từng nhân viên (Loại 1: local)
        {
            "type": "stdio",
            "command": "/Users/macos/.nvm/versions/node/v20.20.0/bin/node",
            "args":    [MEM_PATH],
            "env":     {**os.environ, "MEMORY_FILE_PATH": mem_db},
        },
    ]