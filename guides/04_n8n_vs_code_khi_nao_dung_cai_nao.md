# 04 — n8n (No-Code) vs Viết Code: Khi Nào Dùng Cái Nào?

Sau khi học cả n8n (Tuần 1-2) lẫn Python (Tuần 3-5), nhiều bạn sẽ băn khoăn: "Vậy giờ nên dùng cái nào?" Câu trả lời: **tuỳ bài toán**, không phải cái nào "cao cấp hơn" cái nào.

## Bảng so sánh nhanh

| Tiêu chí | n8n (No/Low-code) | Python (SDK/LangGraph) |
|---|---|---|
| Tốc độ triển khai | Rất nhanh (giờ/ngày) | Chậm hơn (ngày/tuần) |
| Yêu cầu kỹ năng | Không cần biết code | Cần biết lập trình |
| Độ linh hoạt logic | Giới hạn ở các node có sẵn | Không giới hạn |
| Multi-Agent phức tạp, vòng lặp, self-correction | Khó/cồng kềnh | Rất mạnh (đặc biệt LangGraph) |
| Giao diện quản lý trực quan (xem workflow) | Có sẵn, đẹp | Phải tự xây (Gradio, dashboard...) |
| Chi phí duy trì lâu dài | n8n Cloud tính phí theo execution | Chỉ trả phí API, tự host miễn phí |
| Bán cho khách hàng SMB không rành kỹ thuật | Rất phù hợp — dễ bàn giao, dễ chỉnh sửa | Cần đội ngũ kỹ thuật duy trì |
| Custom integration với hệ thống nội bộ phức tạp | Có giới hạn | Toàn quyền kiểm soát |

## Gợi ý lựa chọn theo tình huống thực tế

- **Khách hàng SMB cần tự động hoá nhanh (CSKH, lead, báo cáo định kỳ)** → n8n. Triển khai nhanh, khách có thể tự chỉnh sau khi bàn giao.
- **Cần Agent xử lý logic phức tạp, nhiều bước ra quyết định, tự đánh giá kết quả** → Python + LangGraph (Supervisor, Worker-Evaluator).
- **Cần tích hợp sâu vào hệ thống nội bộ doanh nghiệp (ERP, database riêng)** → Python + MCP Server tự xây.
- **MVP nhanh để test ý tưởng trước khi đầu tư code** → n8n trước, nếu ổn thì "chuyển đổi" logic đó sang Python khi cần mở rộng.

## Một sự thật quan trọng

Ý tưởng phía sau n8n Agent Node và một Agent Python đều **giống nhau**: model + tool + memory + logic ra quyết định. n8n chỉ đang "đóng gói" các khái niệm đó thành giao diện kéo-thả. Đó là lý do khoá học dạy n8n trước — để bạn hiểu bản chất trước khi viết code, thay vì học code từ đầu mà không hiểu vì sao mọi thứ hoạt động như vậy.

Nhiều đội ngũ thực tế **dùng cả hai cùng lúc**: n8n để tự động hoá quy trình nghiệp vụ, gọi vào một Agent Python/LangGraph phức tạp thông qua Webhook hoặc MCP khi cần xử lý logic sâu.
