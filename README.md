# document-prep-starter

![Banner](./assets/banner.svg)

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/document-prep-starter/ci.yml?branch=main&style=for-the-badge)](../../actions)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![License](https://img.shields.io/github/license/eGroupAI/document-prep-starter?style=for-the-badge)](./LICENSE)
[![Starter Kit](https://img.shields.io/badge/Open%20Source-Starter%20Kit-0A7EA4?style=for-the-badge)](#)

> 把文件前處理做成可重用、可測試、可快速接入的開源元件。  
> **公開的是工程能力，不是商業邏輯。**

---

## 專案定位

`document-prep-starter` 是一個「文件前處理 starter kit」，聚焦：

- Markdown / Text 轉換為標準化 chunk JSONL
- 可插拔處理管線（normalize / split / enrich）
- CLI + Python API 雙介面
- CI 與測試可直接跑通

## 公開說明（安全版）

本專案僅提供通用元件說明，不提供實際內部架構圖與流程圖。

## 為什麼會有討論度

- **可立即用**：5 分鐘跑起來，適合 PoC / 黑客松 / 教學場景
- **可擴充**：插件化設計，易於串接你自己的 parser
- **可維運**：CI、測試、版本化、風險邊界一開始就到位
- **可審核**：明確標示哪些內容不在開源範圍，降低誤用風險

---

## 快速開始

### 1) 安裝

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

### 2) 執行前處理

```bash
mdprep ingest --input ./examples/demo.md --output ./out/demo.jsonl --doc-id demo-001
```

### 3) 驗證輸出 schema

```bash
mdprep validate --input ./out/demo.jsonl
```

---

## CLI 指令

```bash
# 轉換檔案 -> JSONL
mdprep ingest --input <PATH> --output <PATH> --doc-id <DOC_ID>

# 驗證 JSONL 結構
mdprep validate --input <PATH>
```

## Python API

```python
from markitdown_prep.core import build_chunks, emit_jsonl

text = "# Hello\n\nThis is a sample."
chunks = build_chunks(text=text, doc_id="sample-001")
emit_jsonl(chunks, "out.jsonl")
```

---

## 輸出格式（JSONL）

每行一筆 JSON，最小欄位：

- `doc_id`
- `chunk_id`
- `text`
- `metadata`（例如 `source`, `char_length`）

---

## 安全邊界（重要）

本 repo **不包含**以下內容：

- 真實客戶資料與內部欄位語意
- 業務流程、業務決策邏輯
- Prompt / 私有詞庫 / 私有後處理規則
- 任何可反推出 production orchestrator 的細節

詳見 `docs/threat-model.md`。

---

## 開發與測試

```bash
pytest -q
```

---

## Roadmap

- [x] v0.1.0：CLI + API + 測試 + CI
- [ ] v0.2.0：Plugin registry
- [ ] v0.3.0：更多 document loader 範例

---

## 公開後討論引導（Launch Playbook）

為了讓公開後更容易形成社群討論，建議在開放 public 時同步執行：

- 發一篇「5 分鐘接入教學」並附可重現指令
- 新增一個 issue：`Showcase your preprocessing pipeline`
- 新增一個 issue：`Benchmark challenge: 10k docs in X minutes`
- 開啟 GitHub Discussions，主題分成 `Showcase / Q&A / Ideas`

---

## 社群熱度飛輪（Hot Loop）

公開後前四週，建議每週固定節奏：

1. 釋出一篇「可重現 demo」貼文（附執行指令）
2. 挑 1 個社群 Showcase 放進 README（建立榮譽感）
3. 回覆所有 issue / discussion（24 小時內）
4. 每週發一個小版本（就算只有文件更新也可以）

完整貼文稿可直接用 `docs/social-launch-kit-zh-TW.md`。

---

## 授權

MIT License，詳見 `LICENSE`。
