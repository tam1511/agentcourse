# 09 — Dùng Model AI Miễn Phí / Giá Rẻ Thay Vì OpenAI

Bạn hoàn toàn có thể học **toàn bộ khoá học** này mà không tốn (hoặc tốn rất ít) chi phí API. Dưới đây là các lựa chọn thay thế OpenAI đã được dùng xuyên suốt khoá học.

## So sánh nhanh các lựa chọn

| Lựa chọn | Chi phí | Tốc độ | Chất lượng | Cần internet? |
|---|---|---|---|---|
| **OpenAI (mini/nano)** | Rất rẻ (~vài cent/session) | Nhanh | Cao, ổn định nhất | Có |
| **Google Gemini (free tier)** | Miễn phí (giới hạn/phút) | Nhanh | Cao | Có |
| **Groq** | Miễn phí (giới hạn/phút) | **Cực nhanh** (LPU) | Tốt (model open-source) | Có |
| **OpenRouter (model `:free`)** | Miễn phí | Trung bình | Tuỳ model | Có |
| **DeepSeek (qua OpenRouter)** | Rất rẻ | Nhanh | Rất tốt, giá tốt nhất/hiệu năng | Có |
| **Ollama (local)** | Hoàn toàn miễn phí | Tuỳ máy | Tuỳ model (nhỏ hơn cloud) | Không cần |

## 1. Google Gemini (miễn phí)

Lấy `GOOGLE_API_KEY` tại https://aistudio.google.com/apikey (xem chi tiết ở [`setup/API-KEYS.md`](../setup/API-KEYS.md)).

Trong OpenAI Agents SDK, bạn có thể trỏ endpoint sang Gemini bằng client tương thích OpenAI:

```python
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

gemini_client = AsyncOpenAI(
    api_key="GOOGLE_API_KEY_CUA_BAN",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)
```

## 2. Groq (miễn phí, siêu nhanh)

Lấy `GROQ_API_KEY` tại https://console.groq.com

```python
groq_client = AsyncOpenAI(
    api_key="GROQ_API_KEY_CUA_BAN",
    base_url="https://api.groq.com/openai/v1"
)
model = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=groq_client)
```

## 3. OpenRouter (một key, nhiều model — kể cả miễn phí)

Lấy `OPENROUTER_API_KEY` tại https://openrouter.ai/keys. Tìm model có hậu tố `:free` trong tên (ví dụ: `meta-llama/llama-3.1-8b-instruct:free`) để dùng hoàn toàn miễn phí.

```python
openrouter_client = AsyncOpenAI(
    api_key="OPENROUTER_API_KEY_CUA_BAN",
    base_url="https://openrouter.ai/api/v1"
)
model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.1-8b-instruct:free",
    openai_client=openrouter_client
)
```

## 4. Ollama — chạy model 100% offline, không cần internet, không tốn phí

Dùng trong Tuần 2, Bài 1.5 ("Tích hợp Ollama vào n8n").

**Cài đặt:**
1. Tải tại https://ollama.com và cài như ứng dụng thông thường
2. Mở terminal, tải một model (ví dụ Llama 3.2):

```bash
ollama pull llama3.2
```

3. Ollama tự chạy server local tại `http://localhost:11434`

**Dùng với OpenAI Agents SDK:**

```python
ollama_client = AsyncOpenAI(
    api_key="ollama",  # giá trị bất kỳ, Ollama không kiểm tra key
    base_url="http://localhost:11434/v1"
)
model = OpenAIChatCompletionsModel(model="llama3.2", openai_client=ollama_client)
```

> Model chạy local sẽ chậm hơn và "kém thông minh" hơn model cloud lớn nếu máy bạn không có GPU mạnh — phù hợp để học và test, không khuyến nghị cho production yêu cầu chất lượng cao.

## Khuyến nghị cho từng giai đoạn học

- **Tuần 1-2 (n8n):** Dùng OpenRouter hoặc Ollama để tiết kiệm tối đa — n8n hỗ trợ cả hai qua node HTTP/Custom Credentials.
- **Tuần 3-5 (Python code):** Dùng OpenAI với model `gpt-4o-mini`/`gpt-4.1-nano` — chi phí cực thấp (dưới 5 USD cho cả 3 tuần) và đảm bảo mọi ví dụ trong khoá học chạy đúng như video. Khi đã quen, tự do thử thay bằng Groq/Gemini/DeepSeek để so sánh.

Toàn bộ code mẫu trong khoá học đều minh hoạ cách đổi qua đổi lại giữa các provider chỉ bằng cách đổi `base_url` và `api_key` — kiến trúc `AsyncOpenAI`-compatible giúp việc này rất đơn giản.
