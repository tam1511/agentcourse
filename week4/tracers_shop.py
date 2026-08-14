"""
tracers_shop.py — Custom Tracer ghi hoạt động agent vào SQLite

Cách hoạt động:
- Subclass TracingProcessor của OpenAI Agents SDK
- Override 4 methods: on_trace_start/end, on_span_start/end
- Mỗi event được ghi vào database với tên nhân viên tương ứng
- Tên nhân viên được extract từ trace_id (format: "ten-HHMMSS")
"""
import secrets, string
from agents import TracingProcessor, Trace, Span
from database_shop import ghi_log

ALPHANUM = string.ascii_lowercase + string.digits


def tao_trace_id(ten_nv: str) -> str:
    """
    Tạo trace_id với tên nhân viên nhúng vào.
    Format: trace_<ten_nv>0<random_suffix>
    Ký tự '0' làm delimiter để extract tên khi đọc log.
    """
    marker = ten_nv.lower() + "0" # "an0", "binh0", "chi0"
    pad = 32 - len(marker)
    suffix = ''.join(secrets.choice(ALPHANUM) for _ in range(pad))
    return f"trace_{marker}{suffix}" #"trace_an0xyz..."


class LogTracer(TracingProcessor):
    """
    Custom tracer: intercept OpenAI trace events → ghi vào SQLite.
    Đây là tính năng extensibility của OpenAI Agents SDK.
    """

    def _lay_ten_nv(self, obj) -> str | None:
        """Extract tên nhân viên từ trace_id."""
        try:
            trace_id = obj.trace_id
            # Format: trace_<ten>0<random>
            # Lấy phần sau "trace_", trước ký tự "0"
            after_prefix = trace_id.split("_", 1)[1] # "an0xyz..."
            if "0" in after_prefix:
                return after_prefix.split("0")[0] # "an"
        except Exception:
            pass
        return None

    def _xay_message(self, obj) -> str:
        """Xây message từ span data."""
        parts = []
        if hasattr(obj, "span_data") and obj.span_data:
            sd = obj.span_data
            if hasattr(sd, "type") and sd.type:
                parts.append(sd.type)
            if hasattr(sd, "name") and sd.name:
                parts.append(sd.name)
            if hasattr(sd, "server") and sd.server:
                parts.append(f"[{sd.server}]")
        if hasattr(obj, "error") and obj.error:
            parts.append(f"LỖI: {str(obj.error)[:80]}")
        return " ".join(parts) if parts else "—"

    def on_trace_start(self, trace: Trace) -> None:
        ten = self._lay_ten_nv(trace)
        if ten:
            ghi_log(ten, "trace", f"Bắt đầu: {trace.name}")

    def on_trace_end(self, trace: Trace) -> None:
        ten = self._lay_ten_nv(trace)
        if ten:
            ghi_log(ten, "trace", f"Kết thúc: {trace.name}")

    def on_span_start(self, span: Span) -> None:
        ten = self._lay_ten_nv(span)
        if ten:
            loai = span.span_data.type if hasattr(span, "span_data") and span.span_data else "span"
            ghi_log(ten, loai, f"Bắt đầu {self._xay_message(span)}")

    def on_span_end(self, span: Span) -> None:
        ten = self._lay_ten_nv(span)
        if ten:
            loai = span.span_data.type if hasattr(span, "span_data") and span.span_data else "span"
            ghi_log(ten, loai, f"Xong {self._xay_message(span)}")

    def force_flush(self) -> None:
        pass

    def shutdown(self) -> None:
        pass