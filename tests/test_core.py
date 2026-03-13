from markitdown_prep.core import build_chunks, normalize_text


def test_normalize_text_trims_and_normalizes() -> None:
    assert normalize_text("ＡＢＣ  \nline ") == "ABC\nline"


def test_build_chunks_creates_stable_ids() -> None:
    chunks = build_chunks("A\n\nB", doc_id="demo")
    assert len(chunks) == 2
    assert chunks[0]["chunk_id"] == "demo-0001"
    assert chunks[1]["chunk_id"] == "demo-0002"
