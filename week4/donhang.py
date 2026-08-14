# donhang.py
import sqlite3
from datetime import datetime
from typing import Optional

DB_PATH = "donhang.db"

def _init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS don_hang (
            id TEXT PRIMARY KEY,
            khach_hang TEXT NOT NULL,
            san_pham TEXT NOT NULL,
            so_luong INTEGER NOT NULL,
            don_gia REAL NOT NULL,
            trang_thai TEXT DEFAULT 'cho_xac_nhan',
            ghi_chu TEXT DEFAULT '',
            ngay_tao TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
class QuanLyDonHang:
    @staticmethod
    def tao_don(khach_hang: str, san_pham: str, so_luong: int, don_gia: float, ghi_chu: str = "") -> dict:
        _init_db()
        conn = sqlite3.connect(DB_PATH)
        ma_don = f"DH{datetime.now().strftime('%Y%m%d%H%M%S')}"
        conn.execute(
            "INSERT INTO don_hang VALUES (?,?,?,?,?,?,?,?)",
            (ma_don, khach_hang, san_pham, so_luong, don_gia, "cho_xac_nhan", ghi_chu, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return {"ma_don": ma_don, "tong_tien": so_luong * don_gia, "trang_thai": "cho_xac_nhan"}

    @staticmethod
    def cap_nhat_trang_thai(ma_don: str, trang_thai: str) -> dict:
        valid = ["cho_xac_nhan", "dang_xu_ly", "dang_giao", "da_giao", "da_huy"]
        if trang_thai not in valid:
            return {"loi": f"Trạng thái không hợp lệ. Chọn: {valid}"}
        conn = sqlite3.connect(DB_PATH)
        conn.execute("UPDATE don_hang SET trang_thai=? WHERE id=?", (trang_thai, ma_don))
        conn.commit()
        conn.close()
        return {"ma_don": ma_don, "trang_thai_moi": trang_thai}

    @staticmethod
    def xem_don(ma_don: str) -> dict:
        conn = sqlite3.connect(DB_PATH)
        row = conn.execute("SELECT * FROM don_hang WHERE id=?", (ma_don,)).fetchone()
        conn.close()
        if not row:
            return {"loi": f"Không tìm thấy đơn {ma_don}"}
        keys = ["ma_don","khach_hang","san_pham","so_luong","don_gia","trang_thai","ghi_chu","ngay_tao"]
        return dict(zip(keys, row))

    @staticmethod
    def danh_sach_don(khach_hang: Optional[str] = None, trang_thai: Optional[str] = None) -> list:
        conn = sqlite3.connect(DB_PATH)
        q, params = "SELECT * FROM don_hang WHERE 1=1", []
        if khach_hang:
            q += " AND khach_hang LIKE ?"; params.append(f"%{khach_hang}%")
        if trang_thai:
            q += " AND trang_thai=?"; params.append(trang_thai)
        rows = conn.execute(q + " ORDER BY ngay_tao DESC", params).fetchall()
        conn.close()
        keys = ["ma_don","khach_hang","san_pham","so_luong","don_gia","trang_thai","ghi_chu","ngay_tao"]
        return [dict(zip(keys, r)) for r in rows]

    @staticmethod
    def doanh_thu(ngay_tu: Optional[str] = None, ngay_den: Optional[str] = None) -> dict:
        conn = sqlite3.connect(DB_PATH)
        q = "SELECT SUM(so_luong*don_gia), COUNT(*) FROM don_hang WHERE trang_thai != 'da_huy'"
        params = []
        if ngay_tu:
            q += " AND ngay_tao >= ?"; params.append(ngay_tu)
        if ngay_den:
            q += " AND ngay_tao <= ?"; params.append(ngay_den + "T23:59:59")
        row = conn.execute(q, params).fetchone()
        conn.close()
        return {"tong_doanh_thu": round(row[0] or 0, 0), "so_don_hang": row[1] or 0}