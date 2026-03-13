"""Public API for document-prep-starter."""

from .core import build_chunks, emit_jsonl, normalize_text

__all__ = ["normalize_text", "build_chunks", "emit_jsonl"]
