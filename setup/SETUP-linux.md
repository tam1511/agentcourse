# Setup Môi Trường Học — Linux

Trước khi bắt đầu coding, có một việc **bắt buộc** phải làm trước: setup environment (môi trường làm việc) cho Data Science, LLMs và Agentic AI.

## Tổng quan 5 bước setup

1. Cài đặt Miniconda
2. Cài đặt IDE (Cursor hoặc IDE bạn quen dùng)
3. Clone source code khoá học bằng Git
4. Tạo virtual environment cho project
5. Thiết lập API keys (`.env`)

---

## 1. Cài đặt Miniconda

Trên Linux, cách nhanh nhất là cài qua terminal:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash   # hoặc zsh nếu bạn dùng zsh
```

Đóng và mở lại terminal, sau đó kiểm tra:

```bash
conda --version
```

Nếu thấy version hiện ra → cài đặt thành công.

> Trang tải chính thức: https://www.anaconda.com/docs/getting-started/anaconda/install — chọn hệ điều hành **Linux** nếu muốn tải bằng GUI installer thay vì dòng lệnh.

---

## 2. Cài đặt IDE — Cursor (tuỳ chọn)

1. Truy cập: https://www.cursor.sh
2. Tải bản `.AppImage` hoặc gói `.deb`/`.rpm` phù hợp với distro của bạn
3. Với AppImage: cấp quyền chạy rồi mở

```bash
chmod +x cursor-*.AppImage
./cursor-*.AppImage
```

**Thiết lập nhanh:** Sau khi mở Cursor, nhấn `Ctrl + Shift + P`, gõ `Shell Command: Install 'code' command`, nhấn Enter. Điều này cho phép mở Cursor từ terminal bằng lệnh `code .`

---

## 3. Clone source code khoá học bằng Git

**Kiểm tra Git** (thường có sẵn trên hầu hết distro):

```bash
git --version
```

Nếu chưa có:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git -y

# Fedora
sudo dnf install git -y

# Arch
sudo pacman -S git
```

**Tạo thư mục chứa project và clone:**

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/tam1511/agentcourse.git
```

---

## 4. Tạo virtual environment cho project

```bash
cd agentcourse
conda env create -f environment.yml
conda activate agents-env
code .
```

> Không dùng conda? Dùng:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> ```

---

## 5. Thiết lập API keys (`.env`)

Tạo file `.env` trong thư mục gốc của project:

```bash
touch .env
```

> File `.env` là **secret**, không được push lên GitHub (đã được loại trừ trong `.gitignore`).

**OpenAI API Key (bắt buộc để học tuần 3–5):**

1. Truy cập: https://platform.openai.com → Billing → nạp tối thiểu 5 USD
2. Tạo API key tại: https://platform.openai.com/api-keys
3. Thêm vào file `.env`:

```
OPENAI_API_KEY=sk-proj-xxxxxxxx
```

**Toàn bộ các API key khác** — xem hướng dẫn chi tiết tại [`API-KEYS.md`](./API-KEYS.md).

---

## Lỗi thường gặp trên Linux

| Lỗi | Cách khắc phục |
|---|---|
| `conda: command not found` sau khi cài | Chạy `source ~/.bashrc` (hoặc `~/.zshrc`) để nạp lại PATH |
| Docker permission denied (khi học Tuần 2 self-host) | `sudo usermod -aG docker $USER` rồi đăng xuất/đăng nhập lại |
| Thiếu `build-essential` khi cài một số thư viện Python | `sudo apt install build-essential python3-dev -y` |

---

## Kiểm tra lại từ đầu

```bash
cd ~/projects/agentcourse
conda activate agents-env
code .
```

Sau đó vào `week1_n8n_nocode/` và bắt đầu coding ngay bây giờ!

---

**Gặp vấn đề?** Xem thêm [`guides/08_troubleshooting.md`](../guides/08_troubleshooting.md) hoặc hỏi trong Q&A khoá học.
