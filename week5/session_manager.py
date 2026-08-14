# session_manager.py

import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional


class PhienLamViec:
    """
    Đại diện cho một phiên làm việc của một người dùng cụ thể.
    Mỗi người dùng có một PhienLamViec riêng biệt hoàn toàn.
    """

    def __init__(self, ma_nguoi_dung: str):
        self.ma_nguoi_dung = ma_nguoi_dung
        self.session_id = str(uuid.uuid4())[:8]
        self.thoi_gian_tao = datetime.now()

        # Thư mục sandbox riêng cho mỗi người dùng
        self.thu_muc_lam_viec = Path(f"./workspaces/{ma_nguoi_dung}")
        self.thu_muc_lam_viec.mkdir(parents=True, exist_ok=True)

        # Thread ID kết hợp mã người dùng + session — đảm bảo unique
        self.thread_id = f"{ma_nguoi_dung}_{self.session_id}"

        self.agent = None  # Sẽ được gán sau
        self.lich_su: list = []

    def __repr__(self):
        return (f"PhienLamViec(nguoi_dung={self.ma_nguoi_dung}, "
                f"session={self.session_id}, "
                f"thread={self.thread_id})")


class QuanLyPhien:
    """
    Quản lý tất cả phiên làm việc đang active.
    Đảm bảo mỗi người dùng không can thiệp vào session của nhau.
    """

    def __init__(self):
        self._phien_active: Dict[str, PhienLamViec] = {}

    def tao_phien_moi(self, ma_nguoi_dung: str) -> PhienLamViec:
        """Tạo phiên làm việc mới cho người dùng."""
        # Nếu đã có phiên cũ, dọn dẹp trước
        if ma_nguoi_dung in self._phien_active:
            self.dong_phien(ma_nguoi_dung)

        phien = PhienLamViec(ma_nguoi_dung)
        self._phien_active[ma_nguoi_dung] = phien
        print(f"[SessionManager] Tạo phiên mới: {phien}")
        return phien

    def lay_phien(self, ma_nguoi_dung: str) -> Optional[PhienLamViec]:
        """Lấy phiên hiện tại của người dùng."""
        return self._phien_active.get(ma_nguoi_dung)

    def dong_phien(self, ma_nguoi_dung: str):
        """Đóng và dọn dẹp phiên của người dùng."""
        if ma_nguoi_dung in self._phien_active:
            phien = self._phien_active.pop(ma_nguoi_dung)
            if phien.agent:
                try:
                    phien.agent.don_dep()
                except Exception as e:
                    print(f"[SessionManager] Lỗi khi dọn dẹp: {e}")
            print(f"[SessionManager] Đã đóng phiên: {ma_nguoi_dung}")

    def so_phien_active(self) -> int:
        return len(self._phien_active)

    def liet_ke_phien(self) -> list:
        return [
            {
                "nguoi_dung": k,
                "session_id": v.session_id,
                "thoi_gian": v.thoi_gian_tao.strftime("%H:%M:%S")
            }
            for k, v in self._phien_active.items()
        ]


quan_ly_phien = QuanLyPhien()