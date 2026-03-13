<div align="center">

<img src="./assets/banner.svg" width="100%" alt="document-prep-starter"/>

<br/>

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/document-prep-starter/ci.yml?branch=main&style=for-the-badge&label=CI)](../../actions)&nbsp;
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](./LICENSE)&nbsp;
[![Free & Open Source](https://img.shields.io/badge/Free%20%26%20Open%20Source-%E2%9C%93-brightgreen?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

**把 `.md` / `.txt` 轉成帶 `chunk_id` 的 JSONL，方便直接接進批次處理或後續 pipeline。**

<br/>

[安裝](#安裝) &nbsp;·&nbsp; [執行](#執行) &nbsp;·&nbsp; [輸出格式](#輸出格式) &nbsp;·&nbsp; [Python API](#python-api) &nbsp;·&nbsp; [授權](#授權)

</div>

---

## 安裝

```bash
python -m venv .venv
. .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

---

## 執行

```bash
# 轉換文件
mdprep ingest --input ./examples/demo.md --output ./out/demo.jsonl --doc-id demo-001

# 驗證輸出格式
mdprep validate --input ./out/demo.jsonl
```

---

## 輸出格式

每行一筆 JSONL，欄位固定：

```json
{"doc_id":"demo-001","chunk_id":"demo-0001","text":"# Demo","metadata":{"source":"public-starter-kit","char_length":6}}
{"doc_id":"demo-001","chunk_id":"demo-0002","text":"這是一份公開示範資料。","metadata":{"source":"public-starter-kit","char_length":11}}
```

---

## Python API

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

本專案採 **[MIT License](./LICENSE)** 授權，**永久免費、可商業使用、可修改、可散佈**。

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)](https://opensource.org/licenses/MIT)
[![Free & Open Source](https://img.shields.io/badge/Free%20%26%20Open%20Source-%E2%9C%93-brightgreen?style=flat-square)](https://opensource.org/licenses/MIT)

| 權利 | 說明 |
| --- | --- |
| ✅ 免費使用 | 個人、商業、學術皆可，不收費 |
| ✅ 可修改 | 可依需求自由調整原始碼 |
| ✅ 可散佈 | 可重新散佈原始或修改版本 |
| ✅ 可商業使用 | 可用於商業產品中 |
| ℹ️ 保留聲明 | 散佈時需保留原始版權與授權聲明 |

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
