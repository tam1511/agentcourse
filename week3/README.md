# Tuần 3 — Lập Trình AI Agent Bằng OpenAI Agents SDK (Python)

> **Mục tiêu tuần này:** Chuyển từ no-code sang code thật. Làm chủ OpenAI Agents SDK: async, multi-agent, structured outputs, guardrails, và tự deploy ứng dụng Agent lên internet.

**Công cụ:** Python · OpenAI Agents SDK · Pydantic · Tavily · Resend · Gradio · HuggingFace Spaces

**Yêu cầu trước khi bắt đầu:** Đã setup môi trường Python (xem [`setup/`](../setup/)). Nên đọc qua [`guides/02_python_co_ban_cho_agent.md`](../guides/02_python_co_ban_cho_agent.md) và [`guides/03_async_python.md`](../guides/03_async_python.md).

---

## Danh sách bài học

### Day 1 — Agent Đầu Tiên Bằng Code
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 1.1 | Vibe Coding: 5 Nguyên Tắc Vàng Để Code Cùng AI Nhanh Gấp 5 Lần | 14:10 | Phương pháp code hiệu quả cùng AI trong Cursor |
| 1.2 | Async Python — Tại Sao AI Agent Bắt Buộc Cần Bất Đồng Bộ | 3:54 | Xem thêm [`guides/03_async_python.md`](../guides/03_async_python.md) |
| 1.3 | Agent, Runner, Trace — Viết AI Agent Đầu Tiên Bằng OpenAI Agents SDK | 18:00 | Ba khái niệm lõi của SDK |
| 1.4 | Đọc Trace Dashboard Như Một Chuyên Gia — Kỹ Năng Debug Agent Quan Trọng | 2:56 | Xem thêm [`guides/07_debug_va_trace.md`](../guides/07_debug_va_trace.md) |
| 1.5 | [DEMO] AI Tư Vấn Sản Phẩm Shopee — Dự Án Thực Tế Đầu Tiên Từ A-Z | 8:18 | Áp dụng ngay vào bài toán TMĐT thật |

### Day 2 — Tools, Song Song Hoá & Multi-Agent
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 2.1 | Trang Bị Công Cụ Cho Agent — Xây Tool Gửi Email Thật Với Resend Từ Đầu | 9:55 | Tool đầu tiên gọi API thật ra ngoài |
| 2.2 | Chạy 3 Agent Song Song Với `asyncio.gather()` — Nhanh Gấp 3 Lần | 2:53 | Tối ưu hiệu năng bằng async |
| 2.3 | Agent-as-Tool vs Handoff — Khi Nào "Nhờ Làm Giúp" Và Khi Nào "Chuyển Giao" | 9:17 | Hai mô hình phối hợp multi-agent |
| 2.4 | [PROJECT] AutoReach Hoàn Chỉnh — Multi-Agent Sales Pipeline | 11:38 | Project multi-agent đầu tiên |

### Day 3 — Đa Dạng Model, Structured Output & Guardrails
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 3.1 | Đa Dạng Hoá Nhà Cung Cấp AI — Kết Nối Groq, Gemini, OpenRouter Miễn Phí | 18:26 | Xem thêm [`guides/09_ai_apis_mien_phi_va_ollama.md`](../guides/09_ai_apis_mien_phi_va_ollama.md) |
| 3.2 | Structured Outputs Với Pydantic — Agent Trả JSON Chuẩn, Không Cần Parse | 4:29 | Đảm bảo output có cấu trúc, đáng tin cậy |
| 3.3 | Guardrails — Xây Lớp Bảo Vệ Chặn Rò Rỉ Thông Tin Nhạy Cảm Cho Agent | 23:35 | Bảo mật và kiểm soát hành vi Agent |
| 3.4 | [DEMO] ReviewBot — Trả Lời Đánh Giá Khách Hàng An Toàn, Tự Định Tuyến | 27:32 | Ứng dụng guardrails + routing thực tế |

### Day 4 — Web Search & Nghiên Cứu Song Song
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 4.1 | Web Search Tool — Cho Agent Tự Lướt Web Với Tavily, Tiết Kiệm 10-15 Lần | 17:43 | Tích hợp Tavily cho tìm kiếm real-time |
| 4.2 | Planner Agent — Tự Động Chia Một Câu Hỏi Lớn Thành 5 Từ Khoá Nghiên Cứu | 5:44 | Kỹ thuật phân rã nhiệm vụ (task decomposition) |
| 4.3 | Tìm Kiếm Song Song 5 Sub-task — 15-20 Giây Xuống Còn 3-4 Giây Với AsyncIO | 5:36 | Tối ưu tốc độ nghiên cứu bằng async |
| 4.4 | [PROJECT] MarketIQ Hoàn Chỉnh — Từ Câu Hỏi Đến Báo Cáo Nghiên Cứu | 12:29 | Project nghiên cứu thị trường tự động |

### Day 5 — Production-Ready & Capstone
| # | Bài học | Thời lượng | Nội dung chính |
|---|---|---|---|
| 5.1 | Tái Cấu Trúc Từ Notebook Sang Python Modules - Trước Khi Ra Sản Phẩm | 13:55 | Chuẩn hoá code cho production |
| 5.2 | Gradio UI — Giao Diện Đẹp Cho Agent, Không Cần Biết Frontend | 12:45 | Xây UI nhanh cho demo/sản phẩm |
| 5.3 | Đọc Trace Dashboard Cho Hệ Thống Multi-Agent Phức Tạp — Debug Như Kỹ Sư | 6:16 | Debug nâng cao cho hệ thống nhiều Agent |
| 5.4 | Deploy Lên HuggingFace Spaces Miễn Phí — Từ Máy Cá Nhân Lên Internet | 13:38 | Đưa sản phẩm lên internet, có link chia sẻ |
| 5.5 | [CAPSTONE] Deep Research App Hoàn Chỉnh | 2:23 | Tổng hợp toàn bộ kiến thức tuần 3 |

---

## Capstone Tuần 3: Deep Research App

Ứng dụng nghiên cứu chuyên sâu hoàn chỉnh: Planner Agent phân rã câu hỏi → tìm kiếm song song bằng Tavily → tổng hợp báo cáo → giao diện Gradio → **deploy công khai trên HuggingFace Spaces**.

## Checklist hoàn thành tuần 3

- [ ] Viết được Agent cơ bản với Agent/Runner/Trace
- [ ] Phân biệt được Agent-as-Tool và Handoff, biết khi nào dùng cái nào
- [ ] Dùng được Structured Output (Pydantic) và Guardrails
- [ ] Chạy được tác vụ song song bằng `asyncio.gather()`
- [ ] Deploy thành công Deep Research App lên HuggingFace Spaces

## Chuẩn bị cho Tuần 4

Tuần 4 đào sâu vào **MCP** — đọc trước [`guides/05_mcp_tong_quan.md`](../guides/05_mcp_tong_quan.md) để có nền tảng.
