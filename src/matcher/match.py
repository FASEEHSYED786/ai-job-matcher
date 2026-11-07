import re

SKILLS = {
    "python": ["python"],
    "rag": ["rag", "retrieval augmented generation", "retrieval-augmented generation"],
    "llm": ["llm", "llms", "large language model"],
    "fastapi": ["fastapi"],
    "langchain": ["langchain"],
    "vector database": ["vector database", "vector db", "pinecone", "weaviate", "qdrant", "chroma", "faiss"],
    "embeddings": ["embedding", "embeddings"],
    "docker": ["docker"],
    "aws": ["aws", "amazon web services"],
    "sql": ["sql", "postgresql", "mysql"],
    "pytorch": ["pytorch"],
    "nlp": ["nlp", "natural language processing"],
    "machine learning": ["machine learning", "ml"],
    "php": ["php"],
    "wordpress": ["wordpress"],
    "kubernetes": ["kubernetes", "k8s"],
    "mlops": ["mlops"],
    "prompt engineering": ["prompt engineering", "prompting"],
}


def extract_skills(text: str) -> set[str]:
    t = " " + re.sub(r"[^a-z0-9+# -]", " ", text.lower()) + " "
    return {skill for skill, aliases in SKILLS.items() if any(f" {a} " in t for a in aliases)}


def score(cv: str, job: str) -> dict:
    have, need = extract_skills(cv), extract_skills(job)
    matched = have & need
    pct = round(100 * len(matched) / len(need), 1) if need else 0.0
    return {"score": pct, "matched": sorted(matched), "missing": sorted(need - have)}


def rank(cv: str, jobs: dict[str, str]) -> list[tuple[str, dict]]:
    return sorted(((n, score(cv, d)) for n, d in jobs.items()), key=lambda x: -x[1]["score"])
