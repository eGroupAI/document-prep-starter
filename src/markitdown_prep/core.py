"""Core preprocessing utilities.

This module intentionally exposes generic preprocessing only.
No business rules, no prompt logic, no proprietary strategies.
"""

from __future__ import annotations

import json
import unicodedata
from pathlib import Path


def normalize_text(text: str) -> str:
    """Normalize text into a stable baseline format."""
    normalized = unicodedata.normalize("NFKC", text)
    lines = [line.rstrip() for line in normalized.splitlines()]
    return "\n".join(lines).strip()


def split_paragraphs(text: str) -> list[str]:
    """Split text by blank lines and drop empty fragments."""
    chunks: list[str] = []
    bucket: list[str] = []
    for line in text.splitlines():
        if line.strip():
            bucket.append(line.strip())
            continue
        if bucket:
            chunks.append(" ".join(bucket))
            bucket = []
    if bucket:
        chunks.append(" ".join(bucket))
    return chunks


def build_chunks(text: str, doc_id: str) -> list[dict[str, object]]:
    """Create normalized chunk records."""
    normalized = normalize_text(text)
    paragraphs = split_paragraphs(normalized)
    return [
        {
            "doc_id": doc_id,
            "chunk_id": f"{doc_id}-{index:04d}",
            "text": paragraph,
            "metadata": {
                "source": "public-starter-kit",
                "char_length": len(paragraph),
            },
        }
        for index, paragraph in enumerate(paragraphs, start=1)
    ]


def emit_jsonl(records: list[dict[str, object]], output_path: str | Path) -> None:
    """Write records to JSONL."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in records:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_text_file(path: str | Path) -> str:
    """Read UTF-8 text file."""
    return Path(path).read_text(encoding="utf-8")
