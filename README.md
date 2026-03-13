# document-prep-starter

![Banner](./assets/banner.svg)

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/document-prep-starter/ci.yml?branch=main&style=for-the-badge)](../../actions)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/eGroupAI/document-prep-starter?style=for-the-badge)](./LICENSE)

> 把 `.md` / `.txt` 轉成帶 `doc_id` + `chunk_id` 的 JSONL，
> 方便直接接進批次處理或後續 pipeline。

---

## 安裝

```bash
python -m venv .venv
# macOS / Linux
. .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -e .[dev]
```

---

## 執行

```bash
# 轉換
mdprep ingest --input ./examples/demo.md --output ./out/demo.jsonl --doc-id demo-001

# 驗證輸出格式
mdprep validate --input ./out/demo.jsonl
```

---

## 輸出長這樣

```json
{"doc_id":"demo-001","chunk_id":"demo-0001","text":"# Demo","metadata":{"source":"public-starter-kit","char_length":6}}
{"doc_id":"demo-001","chunk_id":"demo-0002","text":"這是一份公開示範資料。","metadata":{"source":"public-starter-kit","char_length":11}}
```

每行一筆，欄位固定：`doc_id` / `chunk_id` / `text` / `metadata`。

---

## 如果你要在 Python 裡用

```python
from markitdown_prep.core import build_chunks, emit_jsonl

chunks = build_chunks(text="# Hello\n\nThis is a sample.", doc_id="sample-001")
emit_jsonl(chunks, "out.jsonl")
```

---

## 適合這些情境

- 批次轉換多份文件，輸出統一格式供下游消費
- 自建 ingestion 流程時需要一個有測試的基線
- 只需要拆段 + 標準欄位，不需要額外 dependency

---

## 不包含

- 真實資料與私有欄位定義
- 任何業務規則、決策邏輯、Prompt

詳見 [`docs/threat-model.md`](./docs/threat-model.md)。

---

## 開發

```bash
pytest -q
```

---

## 授權

本專案採 [MIT License](./LICENSE) 授權。

版權所有 © 2026 [eGroupAI 益群健康資訊](https://www.egroupai.com/zh-TW)

---

## 維護者

本 repo 由 **eGroupAI 益群健康資訊** 維護，作為公司開源貢獻的一部分。

| 項目 | 資訊 |
| --- | --- |
| 官網 | [https://www.egroupai.com/zh-TW](https://www.egroupai.com/zh-TW) |
| 聯絡信箱 | [service@egroupai.com](mailto:service@egroupai.com) |
| GitHub 組織 | [github.com/eGroupAI](https://github.com/eGroupAI) |

如有問題或建議，歡迎透過 [GitHub Issues](../../issues) 或上述信箱與我們聯絡。
