# 02 — Python Cơ Bản Cần Biết Trước Tuần 3

Bạn **không cần** là chuyên gia Python để học khoá này, nhưng từ Tuần 3 trở đi (Python SDK, MCP, LangGraph), việc nắm vững những khái niệm dưới đây sẽ giúp bạn tiếp thu nhanh hơn rất nhiều.

## Danh sách khái niệm nên ôn lại

| Khái niệm | Vì sao cần thiết | Ví dụ xuất hiện ở |
|---|---|---|
| Biến, kiểu dữ liệu (str, int, list, dict) | Nền tảng của mọi đoạn code | Toàn bộ khoá học |
| Hàm (function), tham số, giá trị trả về | Mỗi Tool của Agent chính là một hàm Python | Tuần 3-5 |
| `class` và OOP cơ bản | Agent, State thường được định nghĩa bằng class | Tuần 3, 5 |
| Decorator (`@something`) | Cách khai báo Tool: `@tool`, `@function_tool` | Tuần 3, 4, 5 |
| Dictionary & JSON | Dữ liệu trao đổi giữa Agent và Tool | Tuần 1-5 |
| List comprehension | Xử lý danh sách gọn hơn | Tuần 3-5 |
| `try / except` | Xử lý lỗi an toàn khi gọi API | Tuần 3-5 |
| `with open(...) as f` | Đọc/ghi file | Tuần 5 |

## Không cần biết trước, sẽ học trong khoá

- **Async/await** — có hẳn 1 bài riêng dạy từ đầu ([`03_async_python.md`](./03_async_python.md))
- **Pydantic** (structured output) — dạy trực tiếp trong Tuần 3, Bài "Structured Outputs Với Pydantic"
- **LangGraph syntax** (StateGraph, add_node...) — dạy từ đầu trong Tuần 5

## Tài nguyên ôn tập nhanh (nếu cần)

- [Python Official Tutorial](https://docs.python.org/3/tutorial/) — tài liệu chính thức, phần 1-9 là đủ dùng
- [W3Schools Python](https://www.w3schools.com/python/) — học nhanh, có bài tập tương tác

> 💡 Mẹo: Nếu bạn dùng Cursor, cứ mạnh dạn hỏi AI trong Cursor giải thích bất kỳ dòng code Python nào bạn chưa hiểu — đây chính là tinh thần "Vibe Coding" được dạy ở Tuần 3, Bài 1.1.
