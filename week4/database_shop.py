"""
database_shop.py — SQLite helper cho log hoạt động hệ thống CSKH
"""
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = "san_van_cskh.db"

def _init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_nv    TEXT NOT NULL,
            loai      TEXT,
            noi_dung  TEXT,
            tao_luc   TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

_init_db()


def ghi_log(ten_nv: str, loai: str, noi_dung: str):
    """Ghi một dòng log cho nhân viên."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute(
            "INSERT INTO activity_log (ten_nv, loai, noi_dung, tao_luc) VALUES (?,?,?,?)",
            (ten_nv, loai, noi_dung[:300], datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
    except Exception:
        pass  # Log không làm crash hệ thống chính


def doc_log(ten_nv: str, gioi_han: int = 20) -> list:
    """Đọc log gần nhất của một nhân viên."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT loai, noi_dung, tao_luc FROM activity_log "
        "WHERE ten_nv=? ORDER BY id DESC LIMIT ?",
        (ten_nv, gioi_han)
    ).fetchall()
    conn.close()
    return [{"loai": r[0], "noi_dung": r[1], "tao_luc": r[2]} for r in rows]


def doc_log_tat_ca(gioi_han: int = 50) -> list:
    """Đọc log gần nhất của tất cả nhân viên."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT ten_nv, loai, noi_dung, tao_luc FROM activity_log "
        "ORDER BY id DESC LIMIT ?", (gioi_han,)
    ).fetchall()
    conn.close()
    return [{"ten_nv": r[0], "loai": r[1], "noi_dung": r[2], "tao_luc": r[3]} for r in rows]