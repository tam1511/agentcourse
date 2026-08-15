# Hướng Dẫn Lấy Toàn Bộ API Key Cho Khoá Học

File này tổng hợp **tất cả** API key bạn cần trong suốt 5 tuần học, kèm hướng dẫn lấy key từng bước và ghi chú key nào **bắt buộc**, key nào **tuỳ chọn**.

## Tổng quan nhanh

| API Key | Dùng ở tuần | Bắt buộc? | Miễn phí? |
|---|---|---|---|
| `OPENAI_API_KEY` | 3, 4, 5 | Bắt buộc (hoặc thay bằng OpenRouter/Groq/Ollama) | Trả phí (rất rẻ) |
| `RESEND_API_KEY` | 3 | Chỉ khi học bài gửi email | Có gói miễn phí |
| `GROQ_API_KEY` | 3 | Tuỳ chọn (model miễn phí, tốc độ cao) | Miễn phí |
| `GOOGLE_API_KEY` | 3, 2 | Tuỳ chọn (dùng Gemini thay OpenAI) | Có gói miễn phí |
| `OPENROUTER_API_KEY` | 1, 3 | Tuỳ chọn (truy cập nhiều model qua 1 key) | Có model miễn phí |
| `TAVILY_API_KEY` | 3, 4 | Cần cho bài Web Search Agent | Có gói miễn phí |
| `SERPER_API_KEY` | 5 | Cần cho tools tìm kiếm web trong LangGraph | Có gói miễn phí (2.500 lượt) |
| `HF_TOKEN` (Hugging Face) | 3 | Cần khi deploy lên HuggingFace Spaces | Miễn phí |

> **Không muốn tốn tiền?** Bạn hoàn toàn có thể học hết khoá bằng các key miễn phí (Groq, Gemini free tier, OpenRouter free models, Ollama local). Xem [`guides/09_ai_apis_mien_phi_va_ollama.md`](../guides/09_ai_apis_mien_phi_va_ollama.md).

---

## 1. OpenAI API Key

Dùng chính cho Tuần 3–5 (OpenAI Agents SDK, LangGraph).

1. Truy cập https://platform.openai.com
2. Vào **Settings → Billing**, nạp tối thiểu **5 USD**
3. Vào **API Keys**: https://platform.openai.com/api-keys → **Create new secret key**
4. Copy key (chỉ hiện **một lần** — lưu lại ngay)
5. Thêm vào `.env`:

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
```

Theo dõi chi phí tại: https://platform.openai.com/usage

---

## 2. Resend API Key (gửi email thật)

Dùng ở Tuần 3, bài "Trang bị công cụ cho Agent — xây tool gửi email thật với Resend".

1. Truy cập https://resend.com → **Sign Up** (miễn phí, không cần thẻ)
2. Vào **API Keys** → **Create API Key**
3. Đặt tên (vd: `agentcourse`), chọn quyền **Full Access** hoặc **Sending Access**
4. Copy key, thêm vào `.env`:

```
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxx
```

> Gói miễn phí: 100 email/ngày, 3.000 email/tháng — quá đủ để luyện tập.
> Ở chế độ miễn phí/chưa xác minh domain, bạn chỉ có thể gửi đến chính email đã đăng ký tài khoản Resend — điều này là bình thường.

---

## 3. Groq API Key (model miễn phí, siêu nhanh)

Dùng ở Tuần 3, bài "Đa dạng hoá nhà cung cấp AI — kết nối Groq, Gemini, OpenRouter miễn phí".

1. Truy cập https://console.groq.com
2. Đăng nhập bằng Google/GitHub
3. Vào **API Keys** → **Create API Key**
4. Copy key, thêm vào `.env`:

```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

> ⚡ Groq chạy model open-source (Llama, DeepSeek...) trên phần cứng LPU cực nhanh — có gói miễn phí với giới hạn request/phút khá thoải mái cho việc học.

---

## 4. Google API Key (Gemini)

Dùng khi bạn muốn thay OpenAI bằng Gemini (miễn phí) ở nhiều bài trong Tuần 2–3.

1. Truy cập https://aistudio.google.com/apikey
2. Đăng nhập bằng tài khoản Google
3. Nhấn **Create API Key** → chọn project (hoặc tạo project mới)
4. Copy key, thêm vào `.env`:

```
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxx
```

> Google AI Studio có gói miễn phí (giới hạn request/phút) rất phù hợp để học và test.

---

## 5. OpenRouter API Key (một key, truy cập hàng trăm model)

Dùng ở Tuần 1 (bài "Dùng model AI miễn phí với OpenRouter") và Tuần 3.

1. Truy cập https://openrouter.ai
2. Đăng nhập bằng Google/GitHub
3. Vào **Keys** (https://openrouter.ai/keys) → **Create Key**
4. Copy key, thêm vào `.env`:

```
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxx
```

> OpenRouter cho phép gọi hàng trăm model (bao gồm nhiều model **miễn phí**, ký hiệu `:free` trong tên model) chỉ với một API key duy nhất, và một endpoint tương thích chuẩn OpenAI.

---

## 6. Tavily API Key (Web Search cho Agent)

Dùng ở Tuần 3 (bài "Web Search Tool") và Tuần 4.

1. Truy cập https://tavily.com
2. Đăng ký tài khoản miễn phí
3. Vào **Dashboard** → copy API key sẵn có (hoặc tạo key mới)
4. Thêm vào `.env`:

```
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxx
```

> Gói miễn phí: 1.000 lượt tìm kiếm/tháng — được thiết kế riêng cho AI Agent (trả kết quả đã tối ưu cho LLM đọc, không phải HTML thô).

---

## 7. Serper API Key (Web Search cho LangGraph)

Dùng ở Tuần 5, các bài xây tool `tim_kiem_web` trong LangGraph.

1. Truy cập https://serper.dev
2. Đăng ký tài khoản (có thể dùng Google)
3. Vào **Dashboard** → copy API key
4. Thêm vào `.env`:

```
SERPER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Gói miễn phí: 2.500 lượt tìm kiếm — dữ liệu lấy trực tiếp từ Google Search, tốc độ phản hồi rất nhanh.

---

## 8. Hugging Face Token (deploy Agent lên internet)

Dùng ở Tuần 3 (bài "Deploy lên HuggingFace Spaces miễn phí").

1. Truy cập https://huggingface.co → tạo tài khoản miễn phí
2. Vào **Settings → Access Tokens**: https://huggingface.co/settings/tokens
3. **Create new token** → chọn quyền **Write**
4. Copy token, thêm vào `.env`:

```
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
```

> HuggingFace Spaces cho phép deploy ứng dụng Gradio miễn phí, có link public để chia sẻ demo Agent của bạn với bất kỳ ai.

---

## File `.env` hoàn chỉnh mẫu

Tạo file `.env` ở thư mục gốc project với nội dung sau (điền key thật vào, xoá dòng nào bạn không dùng):

```bash
# --- Bắt buộc cho Tuần 3-5 ---
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx

# --- Tuỳ chọn: model thay thế / miễn phí ---
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxx
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxx

# --- Tools & tích hợp ---
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxx
SERPER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# --- Deploy ---
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
```

Xem file mẫu sẵn có tại [`.env.example`](../.env.example) ở thư mục gốc — copy và đổi tên thành `.env` rồi điền key thật vào.

---

## Lưu ý bảo mật quan trọng

- **Không bao giờ** commit file `.env` lên GitHub — repo này đã cấu hình `.gitignore` để tự động loại trừ.
- **Không bao giờ** chia sẻ API key trong ảnh chụp màn hình, video, hoặc gửi qua chat công khai.
- Nếu lỡ làm lộ key, hãy **revoke (thu hồi) ngay lập tức** trên dashboard của nhà cung cấp và tạo key mới.
- Đặt giới hạn chi tiêu (spending limit) trên OpenAI Billing để tránh phát sinh chi phí ngoài ý muốn.

---

**Gặp vấn đề khi lấy key?** Hỏi trong Q&A khoá học hoặc xem [`guides/08_troubleshooting.md`](../guides/08_troubleshooting.md).
