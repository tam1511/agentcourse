import httpx
import json
import sqlite3
import xml.etree.ElementTree as ET
from datetime import date
from typing import Optional, List, Dict, Any
from functools import lru_cache

# ── Cấu hình ──────────────────────────────────────────────────────────────
TIMEOUT = 8  
BDS_DB = "bds_market.db"

def _ngay_hom_nay() -> str:
    return date.today().isoformat()

# ══════════════════════════════════════════════════════════════════════════
# 1. TỶ GIÁ NGOẠI TỆ — VIETCOMBANK (REAL DATA ONLY)
# ══════════════════════════════════════════════════════════════════════════

@lru_cache(maxsize=1)
def _fetch_ty_gia_vcb(ngay: str) -> Dict[str, Any]:
    """Kết nối trực tiếp VCB. Nếu lỗi, raise Exception thay vì dùng mock."""
    url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx"
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            r = client.get(url)
            r.raise_for_status() # Báo lỗi nếu HTTP status != 200
            
            root = ET.fromstring(r.text)
            result = {}
            for exrate in root.findall(".//Exrate"):
                code = exrate.get("CurrencyCode", "")
                result[code] = {
                    "ten_tien": exrate.get("CurrencyName", ""),
                    "mua_tm":   exrate.get("Buy",    "—"),
                    "mua_ck":   exrate.get("Transfer","—"),
                    "ban":      exrate.get("Sell",   "—"),
                }
            return result
    except Exception as e:
        raise ConnectionError(f"Không thể lấy tỷ giá từ Vietcombank: {str(e)}")

def lay_ty_gia(loai_tien: str) -> Dict[str, Any]:
    """Lấy tỷ giá thực tế. Trả về thông báo lỗi nếu không có kết nối."""
    try:
        loai_tien = loai_tien.upper().strip()
        data = _fetch_ty_gia_vcb(_ngay_hom_nay())
        
        if loai_tien not in data:
            return {"loi": f"Mã tiền tệ '{loai_tien}' không tồn tại trong hệ thống VCB."}
            
        info = data[loai_tien]
        return {
            "loai_tien": loai_tien,
            "ten": info["ten_tien"],
            "mua_tm": info["mua_tm"],
            "mua_ck": info["mua_ck"],
            "ban": info["ban"],
            "nguon": "Vietcombank",
            "ngay": _ngay_hom_nay()
        }
    except ConnectionError as ce:
        return {"loi": str(ce)}

# ══════════════════════════════════════════════════════════════════════════
# 2. GIÁ VÀNG — SJC (REAL DATA ONLY)
# ══════════════════════════════════════════════════════════════════════════

@lru_cache(maxsize=1)
def _fetch_gia_vang_sjc(ngay: str) -> List[Dict[str, Any]]:
    """Fetch giá vàng SJC thực tế."""
    url = "https://sjc.com.vn/GoldPrice/Services/PriceService.ashx"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        with httpx.Client(timeout=TIMEOUT, headers=headers) as client:
            r = client.get(url)
            r.raise_for_status()

            data = r.json()
            if isinstance(data, str):
                data = json.loads(data)

            if isinstance(data, dict):
                data = data.get("DataList") or data.get("data") or []

            if not isinstance(data, list):
                raise ValueError("Format dữ liệu SJC không hợp lệ")

            return data

    except Exception as e:
        raise ConnectionError(f"Lỗi kết nối máy chủ SJC: {str(e)}")

def lay_gia_vang(loai_tu_khoa: Optional[str] = None) -> Dict[str, Any]:
    """Tìm giá vàng theo từ khóa (ví dụ: 'SJC', 'Nhẫn', 'PNJ')."""
    try:
        data = _fetch_gia_vang_sjc(_ngay_hom_nay())

        if not data:
            return {"loi": "Không có dữ liệu giá vàng từ SJC"}

        # đảm bảo item là dict
        def is_valid(i):
            return isinstance(i, dict) and "name" in i

        data = [i for i in data if is_valid(i)]

        if not data:
            return {"loi": "Dữ liệu SJC không đúng định dạng"}

        if not loai_tu_khoa:
            item = data[0]
        else:
            item = next(
                (i for i in data if loai_tu_khoa.upper() in i.get("name", "").upper()),
                None
            )

        if not item:
            return {"loi": f"Không tìm thấy loại vàng: {loai_tu_khoa}"}

        return {
            "ten": item.get("name"),
            "mua": f"{float(item.get('buy', 0)):,.0f} VNĐ/lượng",
            "ban": f"{float(item.get('sell', 0)):,.0f} VNĐ/lượng",
            "nguon": "SJC",
            "cap_nhat": _ngay_hom_nay()
        }

    except Exception as e:
        return {"loi": str(e)}

# ══════════════════════════════════════════════════════════════════════════
# 3. BẤT ĐỘNG SẢN — SQLITE LOCAL
# ══════════════════════════════════════════════════════════════════════════

def _init_bds_db():
    """Khởi tạo cấu trúc DB. Dữ liệu mẫu ở đây là 'Seed Data' để test máy local."""
    conn = sqlite3.connect(BDS_DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tin_rao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            khu_vuc TEXT, loai TEXT, dien_tich REAL,
            gia_m2 REAL, gia_tong REAL, tien_ich TEXT,
            ngay_dang TEXT
        )
    """)
    # Chỉ nạp dữ liệu nếu bảng trống (Seed data cho môi trường dev)
    if conn.execute("SELECT COUNT(*) FROM tin_rao").fetchone()[0] == 0:
        mau = [
            ("Quận 7 HCM", "chung_cu", 68, 55e6, 3.74e9, "Gần Crescent Mall"),
            ("Cầu Giấy HN", "chung_cu", 75, 52e6, 3.9e9, "Gần ĐH Quốc Gia"),
            ("Quận 1 HCM", "nha_pho", 50, 300e6, 15e9, "Mặt tiền kinh doanh")
        ]
        conn.executemany(
            "INSERT INTO tin_rao (khu_vuc,loai,dien_tich,gia_m2,gia_tong,tien_ich,ngay_dang) VALUES (?,?,?,?,?,?,?)",
            [(*r, _ngay_hom_nay()) for r in mau]
        )
        conn.commit()
    conn.close()

_init_bds_db()

def tim_bat_dong_san(khu_vuc: str = "", gia_max_ty: float = None) -> List[Dict]:
    """Truy vấn dữ liệu từ DB nội bộ."""
    conn = sqlite3.connect(BDS_DB)
    q, params = "SELECT * FROM tin_rao WHERE 1=1", []
    
    if khu_vuc:
        q += " AND khu_vuc LIKE ?"; params.append(f"%{khu_vuc}%")
    if gia_max_ty:
        q += " AND gia_tong <= ?"; params.append(gia_max_ty * 1e9)
        
    rows = conn.execute(q + " ORDER BY gia_tong DESC", params).fetchall()
    conn.close()
    
    keys = ["id","khu_vuc","loai","dien_tich","gia_m2","gia_tong","tien_ich","ngay_dang"]
    return [dict(zip(keys, r)) for r in rows]

def tinh_roi_cho_thue(gia_mua_ty: float, dien_tich: float, khu_vuc: str) -> Dict:
    """Tính toán hiệu suất đầu tư dựa trên tham số đầu vào."""
    # Logic tính toán thuần túy
    gia_thue_m2_uoc_tinh = 180000 # Giả định trung bình thị trường
    if "Quận 1" in khu_vuc or "Hoàn Kiếm" in khu_vuc:
        gia_thue_m2_uoc_tinh = 350000
        
    thue_thang = dien_tich * gia_thue_m2_uoc_tinh
    yield_rate = (thue_thang * 12) / (gia_mua_ty * 1e9) * 100
    
    return {
        "gia_mua": f"{gia_mua_ty} tỷ",
        "thu_nhap_thang_uoc_tinh": f"{thue_thang:,.0f} VNĐ",
        "ti_suat_loi_nhuan": f"{yield_rate:.2f}%/năm"
    }

def so_sanh_ty_gia(danh_sach_tien: List[str]) -> List[Dict]:
    results = []
    for code in danh_sach_tien:
        results.append(lay_ty_gia(code))
    return results

def tat_ca_gia_vang() -> List[Dict]:
    try:
        return _fetch_gia_vang_sjc(_ngay_hom_nay())
    except:
        return [{"loi": "Không thể lấy toàn bộ bảng giá vàng"}]

def thong_ke_thi_truong(khu_vuc: Optional[str] = None) -> List[Dict]:
    # Mock data thống kê đơn giản để tránh lỗi
    return [{
        "khu_vuc": khu_vuc or "Toàn quốc",
        "loai": "Chung cư",
        "gia_trung_binh": "55tr/m2",
        "so_tin_rao": 150
    }]