from matcher import extract_skills, score, rank

CV = "Python engineer building RAG systems with FastAPI, Docker and PostgreSQL."


def test_extract():
    assert {"python", "rag", "fastapi", "docker", "sql"} <= extract_skills(CV)


def test_score_and_gaps():
    r = score(CV, "We need Python, RAG, Kubernetes and PyTorch.")
    assert r["score"] == 50.0 and r["missing"] == ["kubernetes", "pytorch"]


def test_rank():
    out = rank(CV, {"a": "Kubernetes MLOps", "b": "Python FastAPI RAG"})
    assert out[0][0] == "b"
