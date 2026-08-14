# 06 — So Sánh Các Framework AI Agent

*(Tài liệu tổng kết — nên đọc sau khi hoàn thành Tuần 5)*

Khoá học tập trung sâu vào **n8n**, **OpenAI Agents SDK** và **LangGraph**, nhưng đây không phải là toàn bộ hệ sinh thái. Bảng dưới giúp bạn định vị các lựa chọn khác khi cần.

## Bảng so sánh

| Framework | Mức trừu tượng | Điểm mạnh | Phù hợp khi |
|---|---|---|---|
| **n8n** | No/Low-code | Triển khai cực nhanh, dễ bàn giao cho khách không rành kỹ thuật | Tự động hoá quy trình nghiệp vụ, MVP nhanh |
| **OpenAI Agents SDK** | Cao (agent-first) | Cú pháp gọn, handoff/guardrails có sẵn, tài liệu tốt | Xây Agent/multi-agent gắn liền hệ sinh thái OpenAI |
| **Google ADK** | Cao | Tích hợp tốt với Gemini & hạ tầng Google Cloud | Đội ngũ đã dùng Google Cloud, cần deploy quy mô lớn |
| **CrewAI** | Cao (role-based) | Tư duy "vai trò" (role, goal, backstory) trực quan cho multi-agent | Mô phỏng đội nhóm với vai trò rõ ràng (researcher, writer, reviewer...) |
| **Pydantic AI** | Trung bình-cao | Structured output cực mạnh, type-safe, nhẹ | Cần đảm bảo output luôn đúng schema, ít phụ thuộc framework |
| **LangGraph** | Thấp (low-level, kiểm soát sâu) | Toàn quyền kiểm soát State/Node/Edge, checkpointing, vòng lặp phức tạp | Workflow nhiều nhánh, cần tự đánh giá/tự sửa, Human-in-the-loop |
| **MCP** | Không phải framework Agent | Chuẩn kết nối Agent ↔ Tools/Data | Dùng **cùng với** bất kỳ framework nào ở trên, không thay thế chúng |

## Nguyên lý chọn framework (áp dụng cho mọi trường hợp)

Đừng hỏi "Framework nào tốt nhất?" — hãy hỏi:

1. **Bài toán có thực sự cần Agent không**, hay chỉ cần một pipeline cố định?
2. **Workflow đơn giản hay phức tạp?** Đơn giản → framework cấp cao (OpenAI SDK, CrewAI, ADK) giúp code nhanh. Phức tạp, nhiều nhánh/vòng lặp/tự đánh giá → LangGraph.
3. **Cần kết nối dữ liệu/hệ thống ngoài nào?** → cân nhắc tự xây MCP Server hoặc dùng MCP Server có sẵn.
4. **Ai sẽ maintain hệ thống sau này?** Non-technical → n8n. Technical → framework code.
5. **Hệ sinh thái nào đội ngũ đã quen?** Đã dùng nhiều OpenAI → Agents SDK. Đã dùng Google Cloud → ADK.

## Điều quan trọng nhất cần nhớ

Các framework cấp cao (OpenAI Agents SDK, CrewAI, Google ADK...) về bản chất đều đang **đóng gói lại** những khái niệm cốt lõi mà bạn tự tay xây dựng trong LangGraph: model + tools + state + routing + memory + vòng lặp đánh giá. Học LangGraph ở mức thấp trước giúp bạn hiểu "bên dưới nắp capo" của mọi framework khác — nên khi công cụ mới xuất hiện (và chắc chắn sẽ xuất hiện liên tục), bạn học lại rất nhanh vì nguyên lý không đổi.
