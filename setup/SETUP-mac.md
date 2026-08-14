# 🍎 Setup Môi Trường Học — macOS

Trước khi bắt đầu coding, có một việc **bắt buộc** phải làm trước: setup environment (môi trường làm việc) cho Data Science, LLMs và Agentic AI.

Nếu bỏ qua bước này, bạn rất dễ gặp:
- Lỗi thư viện Python
- Phiên bản không tương thích
- Dependency conflict
- Code chạy được ở máy khác nhưng không chạy được ở máy mình

Vì vậy, chúng ta sẽ setup một môi trường Data Science "xịn sò", dùng xuyên suốt toàn bộ khoá học.

## Tổng quan 5 bước setup

1. Cài đặt Anaconda / Miniconda
2. Cài đặt IDE (Cursor hoặc IDE bạn quen dùng)
3. Clone source code khoá học bằng Git
4. Tạo virtual environment cho project
5. Thiết lập API keys (`.env`)

---

## 1. Cài đặt Anaconda / Miniconda

Nếu bạn từng làm việc với Python hoặc Data Science, có thể bạn đã từng gặp "ác mộng": cài thư viện hôm nay chạy, hôm sau lỗi; version Python không khớp; thư viện xung đột nhau. Đó là lý do chúng ta cần **virtual environment**.

**Vì sao dùng Anaconda / Miniconda?**
- Tạo môi trường Python riêng cho từng project
- Quản lý thư viện AI phức tạp rất dễ (numpy, pandas, scikit-learn, pytorch...)
- Phổ biến trong cộng đồng Data Science & AI

> Nếu bạn lo Anaconda nặng → **Miniconda** là lựa chọn rất tốt, nhẹ hơn nhiều và hoàn toàn đủ cho khoá học này.

**Cách cài đặt:**
1. Truy cập: https://www.anaconda.com/docs/getting-started/anaconda/install
2. Chọn **Miniconda**
3. Chọn hệ điều hành **macOS**
4. Tải về và cài đặt theo hướng dẫn (Next / Agree / Continue)

Sau khi cài xong, mở Terminal và kiểm tra:

```bash
conda --version
```

Nếu thấy version hiện ra → cài đặt thành công.

---

## 2. Cài đặt IDE — Cursor (tuỳ chọn)

Trong khoá học này, mình sẽ sử dụng **Cursor** để minh hoạ. Bạn **không bắt buộc** phải dùng Cursor — VS Code hoặc IDE khác đều hoàn toàn OK.

Cursor là một trải nghiệm mới, có AI hỗ trợ code. Đôi khi gợi ý chưa chính xác, nhưng đáng để thử trong giai đoạn học.

**Cài đặt Cursor:**
1. Truy cập: https://www.cursor.sh
2. Download bản macOS
3. Cài đặt và mở Cursor
4. Khi Cursor hỏi các tuỳ chọn ban đầu → chọn mặc định

**Thiết lập nhanh (rất quan trọng):**

Sau khi mở Cursor, nhấn `Cmd + Shift + P`, gõ:

```
Shell Command: Install 'code' command
```

Nhấn Enter → OK.

Bước này cho phép bạn mở Cursor trực tiếp từ Terminal bằng lệnh `code .`

---

## 3. Clone source code khoá học bằng Git

**Kiểm tra Git:**

macOS thường đã có Git sẵn. Mở Terminal và kiểm tra:

```bash
git --version
```

Nếu chưa có, macOS sẽ gợi ý bạn cài đặt Command Line Tools → chỉ cần đồng ý. Hoặc truy cập https://git-scm.com/install/mac để tải.

**Tạo thư mục chứa project:**

```bash
mkdir ~/projects
cd ~/projects
```

**Clone repo khoá học:**

1. Vào GitHub repo của khoá học
2. Copy HTTPS link
3. Quay lại Terminal:

```bash
git clone https://github.com/tam1511/agentcourse.git
```

Sau khi xong, toàn bộ code của khoá học đã nằm trong máy bạn.

---

## 4. Tạo virtual environment cho project

Vào thư mục project vừa clone:

```bash
cd agentcourse
```

Kiểm tra các file:
- `environment.yml` → dùng cho conda
- `requirements.txt` → dùng nếu bạn không dùng conda

**Tạo môi trường conda:**

```bash
conda env create -f environment.yml
```

Đợi vài phút để cài toàn bộ thư viện.

**Kích hoạt môi trường:**

```bash
conda activate agents-env
```

**Mở project bằng Cursor:**

```bash
code .
```

Cursor sẽ mở đúng thư mục project và dùng môi trường `agents-env`.

> 💡 Không dùng conda? Dùng `venv` + `pip install -r requirements.txt` thay thế — xem hướng dẫn ở README chính.

---

## 5. Thiết lập API keys (`.env`)

Để code chạy mượt mà, chúng ta cần thiết lập API keys.

**Tạo file `.env`:**

Trong thư mục gốc của project → Chuột phải → New File → đặt tên `.env`

> ⚠️ File `.env` là **secret**, chỉ tồn tại trên máy bạn và **không được push lên GitHub**. File `.gitignore` trong repo đã tự động loại trừ file này.

**OpenAI API Key (bắt buộc để học tuần 3–5):**

1. Truy cập: https://platform.openai.com
2. Vào **Billing** và nạp tối thiểu 5 USD
3. Tạo API key tại: https://platform.openai.com/api-keys
4. Thêm vào file `.env`:

```
OPENAI_API_KEY=sk-proj-xxxxxxxx
```

**Toàn bộ các API key khác** (Resend, Groq, Google, OpenRouter, Tavily, Serper, HuggingFace...) — xem hướng dẫn chi tiết từng bước tại [`API-KEYS.md`](./API-KEYS.md).

---

## ✅ Kiểm tra lại từ đầu (khuyến nghị)

Nếu bạn chưa quen, làm lại tuần tự các bước sau mỗi lần mở project:

```bash
cd ~/projects/agentcourse
conda activate agents-env
code .
```

Sau đó vào `week1_n8n_nocode/` (hoặc tuần bạn đang học) và bắt đầu coding ngay bây giờ! 🎉

---

**Gặp vấn đề?** Xem thêm [`guides/08_troubleshooting.md`](../guides/08_troubleshooting.md) hoặc hỏi trong Q&A khoá học.
