# agent_session_aware.py

from tools_module import lay_tat_ca_tools, SANDBOX_DIR
from pathlib import Path


def tao_tools_cho_phien(thu_muc: Path) -> list:
    """
    Tạo một bộ tools mới, với sandbox trỏ đến thư mục của người dùng cụ thể.
    Mỗi người dùng có tools với đường dẫn riêng — không dùng chung.
    """
    from langchain_core.tools import tool
    from langchain_community.utilities import GoogleSerperAPIWrapper
    import os
    from dotenv import load_dotenv
    load_dotenv()

    serper = GoogleSerperAPIWrapper()
    sandbox = thu_muc  # Thư mục riêng của người dùng này

    @tool
    def tim_kiem_web(truy_van: str) -> str:
        """Tìm kiếm thông tin trên internet. Tham số: câu hỏi hoặc từ khóa."""
        try:
            return serper.run(truy_van)
        except Exception as e:
            return f"Lỗi tìm kiếm: {str(e)}"

    @tool
    def doc_file(ten_file: str) -> str:
        """Đọc file từ thư mục làm việc cá nhân. Chỉ dùng tên file, không dùng đường dẫn."""
        duong_dan = sandbox / ten_file
        if not duong_dan.exists():
            files = [f.name for f in sandbox.iterdir() if f.is_file()]
            return f"File không tồn tại. Files có sẵn: {files}"
        return duong_dan.read_text(encoding="utf-8")

    @tool
    def ghi_file(ten_file: str, noi_dung: str) -> str:
        """Ghi nội dung vào file trong thư mục làm việc cá nhân."""
        duong_dan = sandbox / ten_file
        duong_dan.write_text(noi_dung, encoding="utf-8")
        return f"Đã ghi file '{ten_file}' thành công ({duong_dan.stat().st_size} bytes)."

    @tool
    def liet_ke_files() -> str:
        """Xem danh sách files trong thư mục làm việc cá nhân."""
        files = [f.name for f in sandbox.iterdir() if f.is_file()]
        return f"Files của bạn: {files}" if files else "Chưa có file nào."

    return [tim_kiem_web, doc_file, ghi_file, liet_ke_files]