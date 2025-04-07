# test_client_match.py

import json
from mcp.client import get_all_grants
from agent.matcher import match_project_to_grants


def load_project(filepath: str) -> dict:
    """Load project description from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def main():
    # Load sample project
    project = load_project("projects/sample_project.json")

    # Retrieve all grants (from Gitcoin, Devfolio, etc.)
    grants = get_all_grants()

    # Match project to grants
    matches = match_project_to_grants(project, grants)

    print(f"\n🔍 Top Grant Matches for: {project['name']}")
    if matches:
        for match in matches:
            print(f"\n🎯 {match['title']}")
            print(f"Source   : {match['source']}")
            print(f"Tags     : {', '.join(match['tags'])}")
            print(f"Score    : {match['score']}")
            print(f"Deadline : {match['deadline']}")
            print(f"Link     : {match['link']}")
        print("\n✅ Matching complete.\n")
    else:
        print("⚠️  No matching grants found.")

    # Optional Debug: Print all grants
    print("\n📦 All Retrieved Grants:")
    for grant in grants:
        print(f"- {grant['title']} [{grant['source']}]")


if __name__ == "__main__":
    main()
