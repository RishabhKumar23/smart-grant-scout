def match_project_to_grants(project, grants):
    project_tags = set(project.get("tags", []))
    matches = []

    for grant in grants:
        grant_tags = set(grant.get("tags", []))
        score = len(project_tags & grant_tags)  # simple tag overlap

        if score > 0:
            matches.append(
                {
                    "title": grant["title"],
                    "score": score,
                    "link": grant["link"],
                    "tags": list(grant_tags),
                    "deadline": grant["deadline"],
                }
            )

    return sorted(matches, key=lambda x: x["score"], reverse=True)
