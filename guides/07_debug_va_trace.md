# 07 — Debug AI Agent: Đọc Trace Như Một Kỹ Sư

AI Agent là "hộp đen" nếu bạn không có công cụ quan sát đúng. Guide này tổng hợp cách debug ở từng tuần của khoá học.

## Nguyên tắc chung khi debug Agent

1. **Tách nhỏ để test** — đừng test cả hệ thống multi-agent cùng lúc. Test từng Tool/Node độc lập trước (xem Tuần 5, Bài 13 — luôn test tools bằng file `test_tools.py` riêng trước khi gắn vào Agent).
2. **Đọc input/output của từng bước**, không chỉ kết quả cuối cùng.
3. **Kiểm tra docstring/description của Tool** — LLM chọn sai tool hoặc truyền sai tham số thường do mô tả tool không đủ rõ ràng, không phải do model "ngu".
4. **Luôn có giới hạn vòng lặp** (max iterations) khi có Worker-Evaluator hoặc Conditional Edge quay lại chính nó — tránh chạy vô hạn, tốn token.

## Công cụ debug theo từng công nghệ

| Công nghệ | Công cụ debug | Ghi chú |
|---|---|---|
| n8n | Execution log (từng node, xem input/output trực tiếp trên canvas) | Click vào từng node sau khi chạy để xem dữ liệu qua từng bước |
| OpenAI Agents SDK | **Trace Dashboard** (platform.openai.com/traces) | Xem toàn bộ lịch sử gọi model, tool call, handoff của một Runner |
| MCP | Log của MCP Server (stdout/stderr), Custom Tracer tự viết | Tuần 4 dạy cách viết Custom Tracer để log toàn bộ hoạt động vào database |
| LangGraph | **LangSmith** | Xem từng Super Step, prompt đầy đủ, response, token, latency của từng Node |

## Checklist khi Agent trả lời sai/lỗi

- [ ] Prompt (system + user) thực sự gửi cho model là gì? (không phải bạn *nghĩ* là gì)
- [ ] Tool có được gọi đúng không? Tham số truyền vào tool có đúng không?
- [ ] Nếu có nhiều Node/Agent: đúng thứ tự thực thi mong muốn chưa?
- [ ] State ở từng bước có đúng như kỳ vọng không? (đặc biệt trong LangGraph)
- [ ] Có phải do giới hạn context (quá nhiều lịch sử hội thoại) không?
- [ ] Lỗi có tái diễn không, hay chỉ ngẫu nhiên do temperature cao?

## Riêng với LangGraph — 3 lỗi hay gặp nhất

1. **Quên nối Edge quay về Supervisor/Worker sau khi một Node/Tool chạy xong** → graph "kẹt cứng", không biết đi đâu tiếp.
2. **Node trả về toàn bộ State thay vì chỉ phần thay đổi** → phá vỡ nguyên tắc immutable, dữ liệu bị ghi đè sai.
3. **Không giới hạn số vòng lặp Worker-Evaluator** → hai Agent "cãi nhau" vô hạn, tốn rất nhiều token.

👉 Xem chi tiết cách setup LangSmith tại [`week5_langgraph/README.md`](../week5_langgraph/README.md), Bài 8.
