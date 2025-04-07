# agent/matcher.py

from agent.parser import extract_keywords
from rapidfuzz import fuzz

FUZZY_THRESHOLD = 75  # percent similarity for fuzzy matches


def match_project_to_grants(project: dict, grants: list, threshold: int = 1):
    """Match project to grants using exact and fuzzy tag matches."""
    project_keywords = extract_keywords(project["description"])

    scored_matches = []
    for grant in grants:
        grant_tags = [tag.lower() for tag in grant.get("tags", [])]
        score = 0

        for keyword in project_keywords:
            for tag in grant_tags:
                if keyword == tag:
                    score += 2  # Exact match gets higher score
                else:
                    similarity = fuzz.partial_ratio(keyword, tag)
                    if similarity >= FUZZY_THRESHOLD:
                        score += 1

        if score >= threshold:
            scored_matches.append({**grant, "score": score})

    return sorted(scored_matches, key=lambda g: g["score"], reverse=True)
