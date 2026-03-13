"""CLI for document-prep-starter."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import build_chunks, emit_jsonl, load_text_file

REQUIRED_KEYS = {"doc_id", "chunk_id", "text", "metadata"}


def ingest_command(input_path: str, output_path: str, doc_id: str) -> int:
    text = load_text_file(input_path)
    records = build_chunks(text=text, doc_id=doc_id)
    emit_jsonl(records=records, output_path=output_path)
    print(f"[mdprep] wrote {len(records)} chunks to {output_path}")
    return 0


def validate_command(input_path: str) -> int:
    path = Path(input_path)
    if not path.exists():
        print(f"[mdprep] file not found: {input_path}", file=sys.stderr)
        return 1

    line_number = 0
    with path.open("r", encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            payload = json.loads(line)
            missing = REQUIRED_KEYS.difference(payload.keys())
            if missing:
                print(
                    f"[mdprep] line {line_number} missing keys: {sorted(missing)}",
                    file=sys.stderr,
                )
                return 1
    print(f"[mdprep] schema check passed for {line_number} lines")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="document-prep-starter CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    ingest = sub.add_parser("ingest", help="Convert text file to chunk JSONL")
    ingest.add_argument("--input", required=True, dest="input_path")
    ingest.add_argument("--output", required=True, dest="output_path")
    ingest.add_argument("--doc-id", required=True, dest="doc_id")

    validate = sub.add_parser("validate", help="Validate JSONL schema")
    validate.add_argument("--input", required=True, dest="input_path")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "ingest":
        code = ingest_command(
            input_path=args.input_path,
            output_path=args.output_path,
            doc_id=args.doc_id,
        )
        raise SystemExit(code)
    if args.command == "validate":
        code = validate_command(input_path=args.input_path)
        raise SystemExit(code)

    raise SystemExit(2)


if __name__ == "__main__":
    main()
