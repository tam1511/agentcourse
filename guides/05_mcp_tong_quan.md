# 05 — MCP (Model Context Protocol) Tổng Quan

*(Tài liệu tham khảo nhanh — chi tiết đầy đủ nằm trong Tuần 4)*

## MCP là gì, nói một câu?

MCP là một **chuẩn giao tiếp chung** giúp AI Agent kết nối với tools, dữ liệu và hệ thống bên ngoài — giống như USB-C là chuẩn cắm chung cho thiết bị điện tử, thay vì mỗi hãng một loại cổng sạc riêng.

## Vì sao MCP quan trọng?

Trước MCP: mỗi lần muốn Agent dùng một công cụ mới (Slack, Notion, database riêng...), bạn phải tự viết tích hợp riêng cho từng Agent framework. Có MCP: bạn viết **một MCP Server duy nhất**, và bất kỳ Agent/Host nào hỗ trợ MCP (Claude Desktop, Cursor, Agent của bạn...) đều dùng được ngay, không cần viết lại.

## Ba thành phần cốt lõi

| Thành phần | Vai trò | Ẩn dụ nhà hàng (Tuần 4, Bài 1.2) |
|---|---|---|
| **Host** | Ứng dụng người dùng tương tác (Claude Desktop, Agent của bạn) | Khách hàng đặt món |
| **Client** | Cầu nối giữa Host và Server | Nhân viên phục vụ |
| **Server** | Cung cấp Tools, Resources, Prompts thực tế | Nhà bếp — nơi món ăn thực sự được làm ra |

## Ba loại "món" mà MCP Server cung cấp

1. **Tools** — hành động Agent có thể thực hiện (gọi API, ghi database, tính toán...)
2. **Resources** — dữ liệu Agent có thể đọc (file, tài liệu, kết quả truy vấn...)
3. **Prompts** — mẫu prompt dựng sẵn cho các tác vụ lặp lại

## Hai kiểu kết nối chính

- **Stdio** — Server chạy local trên máy, giao tiếp qua input/output chuẩn. Phù hợp công cụ cá nhân, dev local.
- **HTTP Streamable** — Server chạy từ xa (remote), phù hợp triển khai production, nhiều Agent/người dùng cùng kết nối.

## Khi nào tự xây MCP Server, khi nào không cần?

- **Không cần tự xây** nếu: đã có MCP Server có sẵn trong Marketplace đáp ứng đúng nhu cầu (vd: Playwright MCP cho điều khiển trình duyệt), hoặc chỉ cần một vài tool đơn giản → dùng `@function_tool`/`@tool` trực tiếp trong framework Agent là đủ.
- **Nên tự xây** nếu: cần kết nối vào dữ liệu/API nội bộ đặc thù của doanh nghiệp, hoặc muốn tái sử dụng cùng bộ tool cho nhiều Agent/Host khác nhau.

## 5 rủi ro bảo mật cần biết trước khi deploy (chi tiết ở Tuần 4, Bài 1.5)

1. Server độc hại giả mạo tool description để đánh lừa Agent
2. Prompt injection thông qua dữ liệu trả về từ Resource
3. Quyền truy cập quá rộng (Server có thể đọc/ghi ngoài phạm vi cần thiết)
4. Rò rỉ secret/API key khi Server log không cẩn thận
5. Thiếu xác thực (authentication) khi deploy Server ở chế độ HTTP remote

👉 Học chi tiết đầy đủ về kiến trúc, cách tự code MCP Server/Client bằng Python trong [`week4_mcp/README.md`](../week4_mcp/README.md).
