# Setup Môi Trường Học — Windows

Trước khi bắt đầu coding, có một việc **bắt buộc** phải làm trước: setup environment (môi trường làm việc) cho Data Science, LLMs và Agentic AI.

Nếu bỏ qua bước này, bạn rất dễ gặp: lỗi thư viện Python, phiên bản không tương thích, dependency conflict, hoặc "code chạy máy khác nhưng không chạy máy mình".

## Tổng quan 5 bước setup

1. Cài đặt Anaconda / Miniconda
2. Cài đặt IDE (Cursor hoặc IDE bạn quen dùng)
3. Clone source code khoá học bằng Git
4. Tạo virtual environment cho project
5. Thiết lập API keys (`.env`)

---

## 1. Cài đặt Anaconda / Miniconda

**Vì sao dùng Anaconda / Miniconda?**
- Tạo môi trường Python riêng cho từng project, tránh xung đột thư viện
- Quản lý thư viện AI phức tạp rất dễ (numpy, pandas, scikit-learn, pytorch...)
- Phổ biến trong cộng đồng Data Science & AI

> Nếu bạn lo Anaconda nặng → **Miniconda** là lựa chọn nhẹ hơn nhiều, hoàn toàn đủ cho khoá học này.

**Cách cài đặt:**
1. Truy cập: https://www.anaconda.com/docs/getting-started/anaconda/install
2. Chọn **Miniconda**
3. Chọn hệ điều hành **Windows**
4. Tải file `.exe` và cài đặt theo hướng dẫn (Next / I Agree / Install)
5. Tại bước **Advanced Options**, tick chọn **"Add Miniconda3 to my PATH environment variable"** (dù trình cài đặt cảnh báo không khuyến nghị — chọn tick vào sẽ giúp việc dùng lệnh `conda` từ mọi nơi dễ dàng hơn cho người mới)

Sau khi cài xong, mở **Anaconda Prompt** (hoặc Command Prompt / PowerShell nếu đã add vào PATH) và kiểm tra:

```powershell
conda --version
```

Nếu thấy version hiện ra → cài đặt thành công.

---

## 2. Cài đặt IDE — Cursor (tuỳ chọn)

Trong khoá học này, mình sẽ sử dụng **Cursor** để minh hoạ. Bạn **không bắt buộc** phải dùng Cursor — VS Code hoặc IDE khác đều hoàn toàn OK.

**Cài đặt Cursor:**
1. Truy cập: https://www.cursor.sh
2. Download bản Windows
3. Cài đặt và mở Cursor
4. Khi Cursor hỏi các tuỳ chọn ban đầu → chọn mặc định

**Thiết lập nhanh (rất quan trọng):**

Sau khi mở Cursor, nhấn `Ctrl + Shift + P`, gõ:

```
Shell Command: Install 'code' command
```

Nhấn Enter → OK.

Bước này cho phép bạn mở Cursor trực tiếp từ terminal bằng lệnh `code .`

---

## 3. Clone source code khoá học bằng Git

**Kiểm tra Git:**

Windows thường **chưa có Git sẵn**. Mở Command Prompt / PowerShell và kiểm tra:

```powershell
git --version
```

Nếu báo lỗi "not recognized" → tải Git tại: https://git-scm.com/download/win và cài đặt (giữ các tuỳ chọn mặc định khi cài).

> Khuyến nghị: dùng **PowerShell** hoặc **Git Bash** (được cài kèm khi cài Git) thay vì Command Prompt cũ để các lệnh trong khoá học chạy mượt hơn.

**Tạo thư mục chứa project:**

```powershell
mkdir C:\projects
cd C:\projects
```

**Clone repo khoá học:**

1. Vào GitHub repo của khoá học
2. Copy HTTPS link
3. Quay lại terminal:

```powershell
git clone https://github.com/tam1511/agentcourse.git
```

Sau khi xong, toàn bộ code của khoá học đã nằm trong máy bạn.

---

## 4. Tạo virtual environment cho project

Vào thư mục project vừa clone:

```powershell
cd agentcourse
```

Kiểm tra các file: `environment.yml` (dùng cho conda) và `requirements.txt` (dùng nếu không dùng conda).

**Tạo môi trường conda:**

```powershell
conda env create -f environment.yml
```

Đợi vài phút để cài toàn bộ thư viện.

**Kích hoạt môi trường:**

```powershell
conda activate agents-env
```

**Mở project bằng Cursor:**

```powershell
code .
```

> Không dùng conda? Dùng:
> ```powershell
> python -m venv .venv
> .venv\Scripts\activate
> pip install -r requirements.txt
> ```

---

## 5. Thiết lập API keys (`.env`)

**Tạo file `.env`** trong thư mục gốc của project → Chuột phải trong Explorer của Cursor/VS Code → New File → đặt tên `.env`

> File `.env` là **secret**, chỉ tồn tại trên máy bạn và **không được push lên GitHub**.

**OpenAI API Key (bắt buộc để học tuần 3–5):**

1. Truy cập: https://platform.openai.com
2. Vào **Billing** và nạp tối thiểu 5 USD
3. Tạo API key tại: https://platform.openai.com/api-keys
4. Thêm vào file `.env`:

```
OPENAI_API_KEY=sk-proj-xxxxxxxx
```

**Toàn bộ các API key khác** — xem hướng dẫn chi tiết từng bước tại [`API-KEYS.md`](./API-KEYS.md).

---

## Lỗi thường gặp trên Windows

| Lỗi | Cách khắc phục |
|---|---|
| `conda: command not found` sau khi cài | Mở lại **Anaconda Prompt** thay vì Command Prompt thường, hoặc chạy lại installer và tick "Add to PATH" |
| `git: command not found` | Cài Git tại git-scm.com, khởi động lại terminal sau khi cài |
| Lỗi quyền khi activate venv (`.venv\Scripts\activate` bị chặn) | Mở PowerShell với quyền Admin, chạy: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Đường dẫn project có dấu cách hoặc tiếng Việt gây lỗi cài thư viện | Đặt thư mục project ở đường dẫn thuần tiếng Anh, không dấu, không khoảng trắng (vd: `C:\projects\agentcourse`) |

---

## Kiểm tra lại từ đầu (khuyến nghị)

```powershell
cd C:\projects\agentcourse
conda activate agents-env
code .
```

Sau đó vào `week1_n8n_nocode\` (hoặc tuần bạn đang học) và bắt đầu coding ngay bây giờ! 🎉

---

**Gặp vấn đề?** Xem thêm [`guides/08_troubleshooting.md`](../guides/08_troubleshooting.md) hoặc hỏi trong Q&A khoá học.
