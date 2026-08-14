# 03 — Async Python: Vì Sao AI Agent Bắt Buộc Cần Bất Đồng Bộ

*(Tài liệu bổ sung cho Tuần 3, Bài 1.2 — Async Python)*

## Vấn đề cốt lõi

Gọi API đến LLM (OpenAI, Groq...) mất thời gian — có thể vài giây. Nếu bạn gọi tuần tự (đồng bộ) 3 Agent, chương trình sẽ **đợi** Agent 1 xong mới chạy Agent 2, rồi mới đến Agent 3. Tổng thời gian = tổng của cả ba.

Với `async/await`, ba lệnh gọi có thể được **gửi đi cùng lúc** và chờ tất cả trả về song song — tổng thời gian ≈ thời gian của lệnh gọi lâu nhất.

## Ba từ khoá cần nhớ

```python
import asyncio

async def goi_agent(ten: str):          # "async def" — hàm bất đồng bộ
    ket_qua = await mot_ham_khac()       # "await" — chờ kết quả mà không chặn chương trình
    return ket_qua

async def main():
    # Chạy 3 hàm SONG SONG thay vì tuần tự
    ket_qua = await asyncio.gather(
        goi_agent("nghien_cuu"),
        goi_agent("phan_tich"),
        goi_agent("viet_content"),
    )

asyncio.run(main())                      # "asyncio.run()" — điểm khởi động chương trình async
```

## Quy tắc thực dụng (không cần hiểu sâu lý thuyết)

1. Bất kỳ hàm nào gọi API (LLM, web search, HTTP request...) → nên là `async def`.
2. Muốn gọi hàm `async` → phải dùng `await` phía trước.
3. Muốn chạy nhiều tác vụ async **song song** → dùng `asyncio.gather(...)`.
4. Điểm bắt đầu chương trình async → `asyncio.run(main())`.

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
|---|---|---|
| `RuntimeWarning: coroutine was never awaited` | Gọi hàm async nhưng quên `await` | Thêm `await` trước lệnh gọi |
| `SyntaxError: 'await' outside async function` | Dùng `await` trong hàm thường (`def`, không phải `async def`) | Đổi hàm chứa nó thành `async def` |
| Trong Jupyter Notebook báo lỗi loop đang chạy | Notebook đã có event loop sẵn | Dùng `await main()` trực tiếp thay vì `asyncio.run(main())` trong notebook |

## Liên hệ thực tế trong khoá học

- Tuần 3, Bài 2.2: chạy 3 Agent song song bằng `asyncio.gather()` — nhanh gấp 3 lần.
- Tuần 3, Bài 4.3: tìm kiếm song song 5 sub-task — giảm từ 15-20 giây xuống còn 3-4 giây.
- Tuần 5: LangGraph cũng hỗ trợ async cho các Node gọi LLM/tool để tối ưu tốc độ trong hệ Multi-Agent.
