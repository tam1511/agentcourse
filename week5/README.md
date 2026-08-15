# Tuần 5 — LangGraph & Hệ Multi-Agent Chuyên Sâu

> **Mục tiêu tuần này:** Làm chủ LangGraph để kiểm soát workflow phức tạp — State, Checkpointing, Supervisor Pattern, Worker-Evaluator — và khép lại khoá học bằng một Trợ Lý AI Doanh Nghiệp hoàn chỉnh.

**Công cụ:** Python · LangGraph · LangChain · LangSmith · SQLite · Gradio · Serper

**Yêu cầu trước khi bắt đầu:** Đã hoàn thành Tuần 3-4 (quen thuộc với Agent, Tool, async Python).

---

## Danh sách bài học

### Intro
| Bài học | Thời lượng | Mô tả |
|---|---|---|
| LangGraph Là Gì? — Giải Mã Hệ Sinh Thái LangChain | 8:20 | Phân biệt LangChain / LangGraph / LangSmith trước khi bắt đầu — xem thêm [`guides/06_so_sanh_framework_agent.md`](../guides/06_so_sanh_framework_agent.md) |

### Day 1 — Nền Tảng LangGraph: Tư Duy Graph
| Bài | Tiêu đề | Thời lượng | Mô tả |
|---|---|---|---|
| Bài 1 | Vì Sao Chatbot Của Bạn Cần "Suy Nghĩ" Như Con Người | 4:42 | Giới hạn của workflow tuyến tính, vì sao cần tư duy Graph |
| Bài 2 | Ba Viên Gạch Nền Móng — State, Node, Edge | 7:40 | Ba khái niệm cốt lõi, nắm được là hiểu 80% LangGraph |
| Bài 3 | (Mini Project) Xây Chatbot Phân Loại Yêu Cầu Khách Hàng Đầu Tiên | 8:06 | Project đầu tiên dùng Conditional Edge để định tuyến |

### Day 2 — Quản Lý State & Luồng Dữ Liệu
| Bài | Tiêu đề | Thời lượng | Mô tả |
|---|---|---|---|
| Bài 4 | State Bất Biến & Reducer — Vì Sao Không Được Sửa Trực Tiếp | 10:56 | Nguyên lý immutable và Reducer (`add_messages`) |
| Bài 5 | Từ Lý Thuyết Đến Thực Chiến — 5 Bước Dựng Một LangGraph App | 19:19 | Quy trình chuẩn: State → Builder → Node → Edge → Compile |
| Bài 6 | (Mini Project) Agent Tư Vấn TMĐT Biết "Đọc Vị" Khách Hàng | 9:16 | Conditional Edge nâng cao — tự đổi chiến lược theo hành vi khách |

### Day 3 — Bộ Nhớ Thật Sự & Debug Chuyên Nghiệp
| Bài | Tiêu đề | Thời lượng | Mô tả |
|---|---|---|---|
| Bài 7 | Super Step & Checkpointing — Làm Sao Để Agent Không "Mất Trí Nhớ" | 7:12 | Checkpointing với MemorySaver/SQLite |
| Bài 8 | LangSmith — "Chụp X-quang" Bên Trong Đầu Agent | 5:43 | Setup LangSmith để debug — xem [`guides/07_debug_va_trace.md`](../guides/07_debug_va_trace.md) |
| Bài 9 | (Mini Project) Hệ Thống CSKH Phòng Khám — Nhớ Bệnh Nhân Qua Nhiều Ngày | 25:17 | Tool Calling + Checkpointing + LangSmith trong một hệ thống hoàn chỉnh |

### Day 4 — Multi-Agent: Khi Một AI Là Chưa Đủ
| Bài | Tiêu đề | Thời lượng | Mô tả |
|---|---|---|---|
| Bài 10 | Supervisor Pattern — Điều Phối Một Đội Ngũ AI Chuyên Biệt | 23:35 | Structured Output (Pydantic) để điều hướng graph |
| Bài 11 | Worker-Evaluator — Vòng Lặp Giúp AI Tự Sửa Sai | 20:10 | LLM-as-a-Judge — kỹ thuật tự đánh giá và tự cải thiện |
| Bài 12 | (Mini Project) Nhà Máy Sản Xuất Content Marketing Tự Động | 13:25 | Kết hợp Supervisor + Worker-Evaluator thành Agent Harness thu nhỏ |

### Day 5 — Capstone: Trợ Lý AI Doanh Nghiệp Hoàn Chỉnh
| Bài | Tiêu đề | Thời lượng | Mô tả |
|---|---|---|---|
| Bài 13 | Đóng Gói Bộ Công Cụ — Tools Module Chuyên Nghiệp | 14:26 | Tổ chức tools tái sử dụng + sandbox an toàn |
| Bài 14 | Session Isolation — Phục Vụ Hàng Trăm Người Dùng Cùng Lúc | 9:15 | 4 tầng cô lập dữ liệu khi nhiều người dùng chạy song song |
| Bài 15 | **[CAPSTONE] TroLy.AI — Trợ Lý AI Doanh Nghiệp Việt Nam** | 22:09 | Sản phẩm hoàn chỉnh: Tool Calling + Checkpointing + LangSmith + Supervisor + Worker-Evaluator + UI |
| — | Tổng Kết Khoá Học — Tư Duy Về Lựa Chọn Framework | 10:07 | Nhìn lại toàn bộ 5 tuần, cách chọn framework phù hợp cho từng bài toán |

---

## Capstone Tuần 5 & Toàn Khoá Học: TroLy.AI

Trợ lý AI Doanh Nghiệp Việt Nam hoàn chỉnh — một **"Operator Agent"** thực thụ có thể:
- Nghiên cứu thị trường và tự viết báo cáo (lưu file thật)
- Phân tích số liệu kinh doanh, tính KPI
- Soạn thảo nội dung công việc (email, đề xuất, kế hoạch)
- Ghi nhớ ngữ cảnh qua nhiều phiên làm việc (SQLite)
- Tự đánh giá chất lượng output trước khi trả lời (Worker-Evaluator)
- Phục vụ nhiều người dùng đồng thời, dữ liệu tách biệt an toàn

Tài liệu chi tiết tiêu đề & mô tả từng bài (bản mở rộng) xem tại [`../docs/tieu-de-mo-ta-tuan-5-langgraph.md`](../docs/tieu-de-mo-ta-tuan-5-langgraph.md) *(nếu có trong repo của bạn)*.

## Checklist hoàn thành tuần 5 (và cả khoá học!)

- [ ] Hiểu State, Node, Edge, Conditional Edge
- [ ] Biết dùng Reducer và giải thích được nguyên lý immutable
- [ ] Setup được Checkpointing (SQLite) và LangSmith
- [ ] Xây được hệ Supervisor Pattern điều phối nhiều Agent
- [ ] Xây được vòng lặp Worker-Evaluator có giới hạn số vòng
- [ ] Tổ chức được tools thành module riêng, có sandbox an toàn
- [ ] Hiểu 4 tầng Session Isolation cho multi-user
- [ ] Hoàn thành và chạy được TroLy.AI end-to-end

## 🎓 Sau khi hoàn thành khoá học

Bạn đã đi qua hành trình: **no-code (n8n) → code (OpenAI SDK) → kết nối hệ thống (MCP) → kiểm soát workflow sâu (LangGraph)**. Đây không phải 5 công cụ rời rạc — đó là một bản đồ tư duy đầy đủ về cách một hệ thống AI Agent thực sự vận hành. Hãy tiếp tục xây, tiếp tục thử nghiệm — và đừng ngại khi công cụ mới xuất hiện, vì nguyên lý cốt lõi bạn đã nắm sẽ không đổi.
