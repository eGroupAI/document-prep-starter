# document-prep-starter

![Banner](./assets/banner.svg)

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/document-prep-starter/ci.yml?branch=main&style=for-the-badge)](../../actions)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/eGroupAI/document-prep-starter?style=for-the-badge)](./LICENSE)

> 把文件快速轉成可下游使用的標準化 JSONL。  
> **重點是可直接引用，不是概念計畫。**

---

## 一分鐘看懂價值

- 把純文字或 markdown 轉為結構化 chunks
- CLI 與 Python API 都能直接接入
- 有測試與 CI，可快速落地

![Quickstart Preview](./assets/quickstart-preview.svg)

---

## 30 秒快速引用

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
mdprep ingest --input ./examples/demo.md --output ./out/demo.jsonl --doc-id demo-001
mdprep validate --input ./out/demo.jsonl
```

---

## 你可以直接用在

- 文件批次清洗與結構化
- 內部知識整理前置步驟
- 檢索流程的 ingestion baseline

---

## 輸入 / 輸出示例

```text
input:  examples/demo.md
output: out/demo.jsonl
```

```json
{"doc_id":"demo-001","chunk_id":"demo-0001","text":"# Demo","metadata":{"source":"public-starter-kit","char_length":6}}
{"doc_id":"demo-001","chunk_id":"demo-0002","text":"這是一份公開示範資料。","metadata":{"source":"public-starter-kit","char_length":11}}
```

---

## Python API

```python
from markitdown_prep.core import build_chunks, emit_jsonl

text = "# Hello\n\nThis is a sample."
chunks = build_chunks(text=text, doc_id="sample-001")
emit_jsonl(chunks, "out.jsonl")
```

---

## 安全邊界

本 repo 不包含真實資料、業務流程、業務決策規則與內部實作細節。  
詳見 `docs/threat-model.md`。

---

## 開發與測試

```bash
python scripts/keyword_guard.py
pytest -q
```

---

## 授權

MIT License，詳見 `LICENSE`。
