# agent/parser.py

import re
from typing import List


def extract_keywords(description: str) -> List[str]:
    """Extract keywords from a project description using basic NLP."""
    # Lowercase and remove punctuation
    text = re.sub(r"[^\w\s]", "", description.lower())

    # Tokenize
    tokens = text.split()

    # Simple stop words filter
    stop_words = {
        "we",
        "are",
        "the",
        "a",
        "an",
        "for",
        "and",
        "to",
        "of",
        "with",
        "in",
        "like",
        "it",
        "includes",
        "is",
        "on",
        "this",
        "that",
        "our",
        "from",
        "as",
        "by",
        "will",
        "be",
        "using",
    }

    keywords = [token for token in tokens if token not in stop_words and len(token) > 2]

    return list(set(keywords))  # remove duplicates
