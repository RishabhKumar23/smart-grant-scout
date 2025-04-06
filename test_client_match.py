import json
from mcp.client import get_all_grants
from agent.matcher import match_project_to_grants


def main():
    with open("projects/sample_project.json") as f:
        project = json.load(f)

    grants = get_all_grants()
    matches = match_project_to_grants(project, grants)

    print(f"🔍 Top Grant Matches for: {project['name']}")
    for match in matches:
        print(f"\n🎯 {match['title']}")
        print(f"Tags: {', '.join(match['tags'])}")
        print(f"Score: {match['score']}")
        print(f"Link: {match['link']}")
        print(f"Deadline: {match['deadline']}")


if __name__ == "__main__":
    main()
