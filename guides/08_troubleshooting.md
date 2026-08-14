# 08 — Troubleshooting: Các Lỗi Thường Gặp Và Cách Khắc Phục

## 🔧 Lỗi môi trường / setup

| Lỗi | Nguyên nhân thường gặp | Cách khắc phục |
|---|---|---|
| `conda: command not found` | Chưa add conda vào PATH | Mở lại Anaconda Prompt (Windows) hoặc chạy `source ~/.bashrc` (Mac/Linux) |
| `conda env create` chạy rất lâu hoặc treo | Mạng chậm, hoặc conda đang resolve dependency phức tạp | Kiên nhẫn đợi (có thể 5-15 phút lần đầu), hoặc thử `conda config --set channel_priority flexible` |
| `ModuleNotFoundError: No module named 'xxx'` | Chưa activate đúng môi trường, hoặc thư viện chưa được cài | Chạy `conda activate agents-env` trước khi chạy code; kiểm tra `requirements.txt`/`environment.yml` |
| Cursor không nhận đúng Python interpreter | IDE đang trỏ vào Python hệ thống thay vì môi trường conda | Trong Cursor: `Cmd/Ctrl + Shift + P` → "Python: Select Interpreter" → chọn `agents-env` |
| Lệnh `code .` không hoạt động | Chưa cài Shell Command trong Cursor | Xem lại bước "Thiết lập nhanh" trong file SETUP tương ứng hệ điều hành |

## 🔑 Lỗi API Key

| Lỗi | Nguyên nhân | Cách khắc phục |
|---|---|---|
| `AuthenticationError: Incorrect API key` | Key sai, thiếu, hoặc chưa load `.env` | Kiểm tra file `.env` có đúng tên biến không, có gọi `load_dotenv()` trong code chưa |
| `RateLimitError` | Vượt giới hạn request/phút của gói miễn phí | Đợi vài giây rồi thử lại, hoặc nâng cấp gói, hoặc chuyển sang provider khác (Groq/OpenRouter) |
| Key hoạt động trong notebook nhưng không hoạt động khi chạy file `.py` | Notebook có thể đã cache biến môi trường cũ | Restart kernel/terminal, đảm bảo `.env` nằm đúng thư mục gốc project |
| `.env` không được đọc | File đặt sai vị trí, hoặc thiếu `python-dotenv` | Đảm bảo `.env` nằm cùng cấp với file chạy chính; `pip install python-dotenv` |

## 🐳 Lỗi Docker (Tuần 2 — self-host n8n)

| Lỗi | Nguyên nhân | Cách khắc phục |
|---|---|---|
| `Cannot connect to the Docker daemon` | Docker Desktop chưa mở | Mở ứng dụng Docker Desktop, đợi biểu tượng chuyển sang "Running" |
| `port is already allocated` | Port 5678 (mặc định n8n) đang bị chiếm | Đổi port trong `docker-compose.yml`, hoặc tắt tiến trình đang dùng port đó |
| Permission denied trên Linux | User chưa thuộc group `docker` | `sudo usermod -aG docker $USER` rồi đăng xuất/đăng nhập lại |

## 🧩 Lỗi khi chạy Agent (Tuần 3-5)

| Lỗi | Nguyên nhân | Cách khắc phục |
|---|---|---|
| Agent lặp vô hạn giữa các bước | Thiếu điều kiện dừng/giới hạn vòng lặp | Thêm giới hạn `max_turns`/đếm số vòng, kiểm tra Conditional Edge có route đến `END` đúng chưa |
| Agent gọi sai Tool hoặc không gọi Tool khi cần | Docstring/description của Tool chưa đủ rõ | Viết lại description: mô tả rõ **khi nào dùng**, **tham số là gì**, ví dụ cụ thể |
| `RuntimeWarning: coroutine was never awaited` | Quên `await` khi gọi hàm async | Xem [`03_async_python.md`](./03_async_python.md) |
| LangGraph báo lỗi thiếu Node/Edge khi compile | Quên `add_edge()` nối một Node vào graph | Kiểm tra lại toàn bộ Node đã có ít nhất 1 đường vào và 1 đường ra |
| Output của Structured Output (Pydantic) không đúng schema | Model chưa được cấu hình `with_structured_output`/`response_format` | Kiểm tra đã bind đúng schema Pydantic vào LLM instance chưa |

## Vẫn chưa giải quyết được?

1. Đọc kỹ lại thông báo lỗi đầy đủ (traceback) — thường chỉ rõ dòng code gây lỗi.
2. Thử hỏi trực tiếp AI trong Cursor, dán nguyên traceback vào để được giải thích.
3. Đặt câu hỏi trong phần **Q&A của khoá học trên Udemy** kèm: mô tả lỗi, đoạn code liên quan, và bạn đã thử cách nào.
