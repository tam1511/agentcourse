# Tuần 2 — Self-Host n8n, OAuth2 Nâng Cao & MCP Nhập Môn

> 🎯 **Mục tiêu tuần này:** Tự host n8n bằng Docker, chạy model AI miễn phí/offline (DeepSeek, Ollama), làm chủ Google OAuth2, và bắt đầu làm quen với MCP — chuẩn kết nối Agent đang thay đổi cả ngành.

**Công cụ:** Docker Desktop · n8n self-host · Ollama · Google OAuth2 · Firecrawl · MCP

**Yêu cầu trước khi bắt đầu:** Đã hoàn thành Tuần 1. Cài Docker Desktop (xem [`setup/`](../setup/)).

---

## 📋 Danh sách bài học

### Day 1 — Self-Host & Model Miễn Phí
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 1.1 | n8n Cloud vs Self-Hosted: Framework 4 Câu Hỏi Để Ra Quyết Định Đúng | 8:04 | Khung ra quyết định khi nào nên tự host |
| 1.2 | Cài n8n Local Bằng Docker Desktop — Từng Bước Cho Cả Mac Và Windows | 3:33 | Setup nhanh bằng Docker Desktop GUI |
| 1.3 | Chạy n8n Bằng Docker Compose — Setup Production-Ready Trên Máy Của Bạn | 7:42 | Cấu hình bền vững hơn cho production |
| 1.4 | Kết Nối AI Agent Với DeepSeek R1 Qua OpenRouter Trên n8n Self-Host | 1:42 | Model giá rẻ, chất lượng cao |
| 1.5 | Tích Hợp Ollama Vào n8n — AI Agent Chạy 100% Offline, Không Tốn Phí API | 6:10 | Agent chạy hoàn toàn local, miễn phí |

### Day 2 — Google OAuth2, Scraping & CRM Mini
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 2.1 | Google OAuth2 Từ A-Z: Mở Khoá Toàn Bộ Hệ Sinh Thái Drive, Gmail, Sheet | 16:50 | Xác thực chuẩn cho mọi tích hợp Google |
| 2.2 | Agent Tự Đọc PDF Từ Google Drive — Trích Xuất Hồ Sơ KH Tự Động | 7:33 | Tự động hoá xử lý tài liệu |
| 2.3 | Firecrawl API: Thu Thập Dữ Liệu Đối Thủ & Structured Outputs | 9:16 | Web scraping có cấu trúc cho AI |
| 2.4 | Xây CRM Mini: Form Đăng Ký → Google Sheets → AI Soạn Tin Nhắn Cá Nhân | 20:55 | Pipeline CRM tự động hoàn chỉnh |
| 2.5 | HTTP Request Node & Structured Output Nâng Cao | 1:22 | Kỹ thuật gọi API tuỳ chỉnh |

### Day 3 — MCP Nhập Môn
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 3.1 | MCP Là Gì? Hiểu Đúng Bản Chất Giao Thức Đang Thay Đổi Cách AI Dùng Tool | 6:52 | Nền tảng MCP — xem thêm [`guides/05_mcp_tong_quan.md`](../guides/05_mcp_tong_quan.md) |
| 3.2 | Kiến Trúc MCP Sâu Hơn: Stdio vs HTTP Streamable, Marketplace Server | 7:18 | Hai kiểu kết nối, kho MCP Server có sẵn |
| 3.3 | Kết Nối Firecrawl Qua MCP — Xây Prospecting Sub-agent Tự Tìm KH B2B | 11:51 | Ứng dụng MCP thực tế đầu tiên |
| 3.4 | Tự Xây MCP Server Trong n8n Và Kết Nối Trực Tiếp Với Claude | 11:28 | Tự tạo MCP Server ngay trong n8n |

### Day 4 — Hệ Sub-Agent Bán Hàng Tự Động
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 4.1 | (1) Operations Sub-agent — Tự Động Ghi Lead Vào CRM Với Structured Output | 8:47 | Sub-agent chuyên trách vận hành |
| 4.2 | (2) Sales Sub-agent — AI Tự Soạn Email & Xếp Hàng Tin Nhắn Zalo | 7:39 | Sub-agent chuyên trách sales |
| 4.3 | (3) Business Development Manager — Ghép 3 Sub-agent Thành Pipeline Tự Động | 14:21 | Điều phối nhiều sub-agent |
| 4.4 | (4) Learning Advisor — Sub-agent Ghi Nhận Deal & Đặt Lịch Tư Vấn | 17:05 | Hoàn thiện pipeline 4 sub-agent |
| 4.5 | AI Voice Agent Tiếng Việt — Nghe Điện Thoại, Ghi CRM Và Đặt Lịch 24/7 | 17:04 | Capstone: Voice Agent tiếng Việt hoàn chỉnh |

---

## 🏆 Capstone Tuần 2: Hệ Thống Sales Pipeline 4 Sub-Agent + Voice Agent

Một hệ thống tự động hoá bán hàng hoàn chỉnh gồm 4 sub-agent chuyên biệt (Operations, Sales, BDM, Learning Advisor) phối hợp qua một pipeline, kết hợp AI Voice Agent tiếng Việt nghe điện thoại và tự ghi nhận vào CRM.

## ✅ Checklist hoàn thành tuần 2

- [ ] Tự host được n8n bằng Docker (Desktop hoặc Compose)
- [ ] Kết nối được ít nhất 1 model miễn phí (DeepSeek/Ollama)
- [ ] Hiểu và cấu hình được Google OAuth2
- [ ] Hiểu kiến trúc MCP (Host/Client/Server) và kết nối được 1 MCP Server
- [ ] Hoàn thành hệ thống 4 Sub-agent + Voice Agent

## 🔜 Chuẩn bị cho Tuần 3

Từ Tuần 3, khoá học chuyển hẳn sang **viết code Python**. Đảm bảo đã hoàn thành setup môi trường ở [`setup/`](../setup/) (Anaconda/Miniconda + Cursor + `.env`).
