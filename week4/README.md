# Tuần 4 — Model Context Protocol (MCP) Chuyên Sâu

> 🎯 **Mục tiêu tuần này:** Tự xây MCP Server/Client bằng Python, kết nối Agent với dữ liệu và API thực tế của doanh nghiệp, và xây dựng một hệ thống CSKH gồm 4 "AI nhân viên" phối hợp qua MCP.

**Công cụ:** Python · MCP SDK · Tavily MCP · Custom Tracer · Gradio

**Yêu cầu trước khi bắt đầu:** Đã hoàn thành Tuần 3. Đọc lại [`guides/05_mcp_tong_quan.md`](../guides/05_mcp_tong_quan.md) nếu cần ôn nhanh.

---

## 📋 Danh sách bài học

### Day 1 — Kiến Trúc MCP & Kết Nối Đầu Tiên
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 1.1 | What is MCP? Và Tại Sao Nó Thay Đổi Cuộc Chơi | 6:48 | Bối cảnh và tầm quan trọng của MCP |
| 1.2 | Kiến Trúc Host — Client — Server Qua Ẩn Dụ Nhà Hàng Việt Nam | 10:32 | Ba thành phần lõi, dễ hiểu qua ẩn dụ |
| 1.3 | Kết Nối MCP Server Đầu Tiên — Từ Cài Đặt Đến Agent Nghiên Cứu Thị Trường | 18:46 | Thực hành kết nối MCP Server có sẵn |
| 1.4 | Khám Phá MCP Marketplace — Hơn 200 Công Cụ Miễn Phí Đang Chờ | 5:07 | Kho MCP Server có sẵn để tái sử dụng |
| 1.5 | Bảo Mật MCP: 5 Rủi Ro Bắt Buộc Phải Biết Trước Khi Deploy | 9:22 | Checklist an toàn trước khi triển khai thật |

### Day 2 — Tự Xây MCP Server & Client
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 2.1 | Khi Nào Thực Sự Cần Tự Xây MCP Server? (Và Khi Nào Chỉ Cần `@function_tool`) | 4:50 | Ra quyết định đúng, tránh over-engineering |
| 2.2 | Giải Phẫu MCP Server: Tools, Resources, Prompts | 6:38 | Ba thành phần một MCP Server cung cấp |
| 2.3 | Code MCP Server Đầu Tiên Bằng Python — Tách Biệt Business Logic | 11:40 | Viết Server từ đầu, kiến trúc sạch |
| 2.4 | Nhúng Business Logic Thực Tế — Agent Tự Tạo Đơn, Cập Nhật Trạng Thái | 9:54 | Kết nối MCP với nghiệp vụ thật |
| 2.5 | Tự Xây MCP Client Từ Đầu — Hiểu Điều SDK Đang Làm Thay Bạn | 12:49 | Hiểu sâu cơ chế phía dưới SDK |

### Day 3 — Kết Nối API Bên Ngoài & Dữ Liệu Việt Nam
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 3.1 | Patterns Khi MCP Server Gọi API Bên Ngoài — 4 Nguyên Tắc Bắt Buộc | 5:59 | Best practice khi Server gọi ra ngoài |
| 3.2 | Build MCP Server Dữ Liệu Tài Chính Việt Nam — Tỷ Giá Vietcombank, BĐS | 5:59 | Ứng dụng thực tế cho thị trường VN |
| 3.3 | Lab: Ba Loại MCP Server, Một Dự Án — Memory, Dữ Liệu VN, Và Tavily | 6:29 | Kết hợp nhiều Server trong một Agent |
| 3.4 | [PROJECT] Agent Phân Tích Đầu Tư Bất Động Sản HCM/Hà Nội | 6:24 | Project ứng dụng dữ liệu thật |

### Day 4 — Thiết Kế Hệ Thống Đa Agent
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 4.1 | Thiết Kế Hệ Thống Trước Khi Code — 5 Câu Hỏi Cho Đội Ngũ 4 Agent CSKH | 7:35 | Tư duy thiết kế trước khi viết code |
| 4.2 | Lab: Thử Nghiệm Từng Thành Phần — Từ Researcher Độc Lập Đến Nhân Viên | 6:36 | Test từng Agent riêng lẻ trước khi ghép |
| 4.3 | Đóng Gói Module Production: `nhan_vien.py` — Từ Notebook Đến Class | 4:02 | Chuẩn hoá code production |
| 4.4 | 10 Bài Học Khi Xây MCP Thực Tế — Từ Kinh Nghiệm Triển Khai Thật | 5:15 | Kinh nghiệm thực chiến, tránh sai lầm phổ biến |

### Day 5 — Hoàn Thiện Hệ Thống & Capstone
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 5.1 | Custom Tracer — "Nghe Lén" Mọi Hoạt Động Của Agent Và Ghi Vào Database | 7:19 | Xây công cụ observability riêng |
| 5.2 | Bộ Điều Phối Trung Tâm `san_van_cskh.py` — Trái Tim Vận Hành Của Hệ Thống | 4:26 | Orchestrator điều phối 4 Agent |
| 5.3 | Lab: Kết Nối Tất Cả — Từ Custom Tracer Đến Đếm Tổng 42 Tools | 4:13 | Ghép toàn bộ hệ thống lại với nhau |
| 5.4 | Gradio UI & Chạy Production Thật — Xem 4 AI Nhân Viên Làm Việc | 5:08 | Capstone hoàn chỉnh, có giao diện thật |

---

## 🏆 Capstone Tuần 4: Hệ Thống CSKH 4 "AI Nhân Viên"

Một hệ thống CSKH hoàn chỉnh với 4 Agent chuyên biệt phối hợp qua MCP Server tự xây, tổng cộng **42 tools**, có Custom Tracer ghi lại toàn bộ hoạt động vào database, và giao diện Gradio để vận hành thật.

## ✅ Checklist hoàn thành tuần 4

- [ ] Hiểu và giải thích được kiến trúc Host — Client — Server
- [ ] Tự viết được một MCP Server Python từ đầu (Tools + Resources)
- [ ] Tự viết được một MCP Client cơ bản
- [ ] Biết 5 rủi ro bảo mật cần kiểm tra trước khi deploy MCP Server
- [ ] Hoàn thành hệ thống CSKH 4 Agent với Custom Tracer

## 🔜 Chuẩn bị cho Tuần 5

Tuần cuối cùng — **LangGraph** — sẽ đào sâu vào kiểm soát workflow multi-agent phức tạp. Xem trước [`week5_langgraph/README.md`](../week5_langgraph/README.md).
