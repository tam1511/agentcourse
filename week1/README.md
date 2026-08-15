# Tuần 1 — AI Agent No-Code Với n8n

> **Mục tiêu tuần này:** Hiểu bản chất một AI Agent (model + memory + tool) và tự xây được Agent đầu tiên, tích hợp Gmail/Sheets/Telegram/Slack — hoàn toàn không cần biết code.

**Công cụ:** n8n Cloud · OpenAI · OpenRouter

**Yêu cầu trước khi bắt đầu:** Không cần biết lập trình. Chỉ cần tài khoản n8n Cloud (bản dùng thử miễn phí) và Gmail/Google.

---

## 📋 Danh sách bài học

### Day 1 — Nhập môn & Nền tảng
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 1.1 | Demo Trực Tiếp: Xây AI Agent Đầu Tiên Trên n8n Trong 8 Phút (No code) | 8:35 | Xem toàn cảnh một Agent hoàn chỉnh chạy thật trước khi học chi tiết |
| 1.2 | Lộ Trình 5 Tuần & Bạn Sẽ Đạt Được Gì Sau Khoá Học Này | 6:11 | Roadmap tổng thể, kỳ vọng đầu ra từng tuần |
| 1.3 | Nền Tảng Bắt Buộc: GenAI, LLM, API và Định Nghĩa Đúng Về AI Agent | 6:41 | Khái niệm cốt lõi — phân biệt chatbot thường và AI Agent thực sự |
| 1.4 | n8n Cloud vs Self-Hosted: Chọn Đúng Phiên Bản Cho Giai Đoạn Của Bạn | 5:27 | Tiêu chí lựa chọn nền tảng phù hợp với nhu cầu |

### Day 2 — Agent Đầu Tiên & Context Engineering
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 2.1 | Xây AI Agent Đầu Tiên Với OpenAI: Model + Memory + Tool (Weather Agent) | 14:19 | Project thực hành đầu tiên — 3 thành phần lõi của mọi Agent |
| 2.2 | Dùng Model AI Miễn Phí Với OpenRouter — Không Tốn Một Đồng API Nào | 4:21 | Tiết kiệm chi phí học tập với model free |
| 2.3 | System Prompt, User Prompt và Context Engineering | 15:52 | Kỹ thuật viết prompt quyết định chất lượng Agent |
| 2.4 | Sub-agents: Khi Nào Nên Chia Nhỏ Một AI Agent (Và Khi Nào Không Nên) | 6:38 | Nguyên tắc thiết kế — tránh over-engineering |

### Day 3 — Tích Hợp Dữ Liệu & Kênh Giao Tiếp
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 3.1 | Agent Đọc & Ghi Google Sheets Thời Gian Thực — Phân Tích Dữ Liệu | 10:30 | Kết nối Agent với dữ liệu doanh nghiệp |
| 3.2 | Hiểu JSON Trong n8n: Key-Value, Object, Array và Cấu Trúc Lồng Nhau | 6:31 | Nền tảng dữ liệu bắt buộc phải nắm |
| 3.3 | AI Agent Tự Đọc Email & Soạn Draft Trả Lời Khách Hàng Trên Gmail | 8:18 | Tự động hoá CSKH qua email |
| 3.4 | Expressions & Authentication Trong n8n: Từ API Key Đến OAuth2 Đầy Đủ | 7:04 | Kỹ thuật xác thực nâng cao |
| 3.5 | Xây Telegram Bot Kinh Doanh 24/7 — Từ BotFather Đến Production | 11:48 | Kênh chat tự động phục vụ khách 24/7 |
| 3.6 | Tích Hợp Slack Cho Doanh Nghiệp: OAuth2 + Webhook Từ A Đến Z | 13:21 | Tự động hoá thông báo/vận hành nội bộ |

### Day 4 — Capstone Tuần 1
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 4.1 | Capstone Tuần 1 (Phần 1): Thiết Kế Smart Business Dashboard Từ Đầu | 13:47 | Thiết kế hệ thống trước khi build |
| 4.2 | (Phần 2): Tool Description Chuẩn — Yếu Tố Quyết Định Agent Đáng Tin Cậy | 3:45 | Kỹ thuật viết mô tả Tool chuẩn |
| 4.3 | Thêm IF/ELSE Để Agent Tự Phân Loại Cảnh Báo Normal/Warning/Critical | 8:38 | Logic rẽ nhánh trong workflow |
| 4.4 | Deploy Production: Biến Workflow Thành Sản Phẩm Có Thể Gửi Cho Khách Hàng | 5:55 | Từ demo cá nhân → sản phẩm bàn giao được |

---

## Capstone Tuần 1: Smart Business Dashboard

Một hệ thống n8n hoàn chỉnh: Agent tự đọc dữ liệu kinh doanh, phân loại mức độ cảnh báo (Normal/Warning/Critical) và có thể **triển khai thật, gửi cho khách hàng sử dụng ngay**.

## Checklist hoàn thành tuần 1

- [ ] Hiểu 3 thành phần lõi của Agent: model, memory, tool
- [ ] Biết viết System Prompt + User Prompt hiệu quả
- [ ] Kết nối được Agent với ít nhất 2 trong số: Gmail, Sheets, Telegram, Slack
- [ ] Hoàn thành Smart Business Dashboard và deploy được workflow

## Chuẩn bị cho Tuần 2

Tuần 2 sẽ chuyển sang **self-host n8n bằng Docker** — cài đặt Docker Desktop trước nếu muốn học mượt hơn (không bắt buộc, sẽ hướng dẫn từ đầu).
