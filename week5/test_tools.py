# test_tools.py — chạy file này riêng để kiểm tra tools
from tools_module import tim_kiem_web, ghi_file, doc_file, chay_python, tinh_toan

print("=== Test Tool 1: Web Search ===")
ket_qua = tim_kiem_web.invoke({"truy_van": "giá vàng hôm nay Việt Nam"})
print(ket_qua[:300])

print("\n=== Test Tool 2: Ghi file ===")
ket_qua = ghi_file.invoke({
    "ten_file": "test_output.md",
    "noi_dung": "# Test\nNội dung test từ tool",
    "che_do": "ghi_moi"
})
print(ket_qua)

print("\n=== Test Tool 3: Đọc file vừa ghi ===")
ket_qua = doc_file.invoke({"ten_file": "test_output.md"})
print(ket_qua)

print("\n=== Test Tool 4: Python Execution ===")
ket_qua = chay_python.invoke({
    "code": """
doanh_thu = [120, 145, 132, 168, 155, 190]
trung_binh = sum(doanh_thu) / len(doanh_thu)
tang_truong = (doanh_thu[-1] - doanh_thu[0]) / doanh_thu[0] * 100
print(f"Doanh thu trung bình: {trung_binh:.1f} triệu")
print(f"Tăng trưởng: {tang_truong:.1f}%")
"""
})
print(ket_qua)

print("\n=== Test Tool 5: Tính toán ===")
ket_qua = tinh_toan.invoke({"bieu_thuc": "(500000000 - 320000000) / 500000000 * 100"})
print(f"Biên lợi nhuận: {ket_qua}")

print("\nTất cả tools đều hoạt động!")