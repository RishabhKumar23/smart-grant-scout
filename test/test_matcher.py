# tests/test_matcher.py

from agent.matcher import match_project_to_grants


def test_matching_logic():
    project = {
        "name": "ZK Identity Infra",
        "description": "We're building privacy-preserving identity infra using zk-SNARKs and DID protocols.",
    }

    grants = [
        {
            "title": "Privacy Grant",
            "description": "Support zk identity and private infrastructure.",
            "tags": ["zk", "identity", "privacy"],
            "deadline": "2024-05-10",
            "link": "https://example.com",
            "source": "gitcoin",
        },
        {
            "title": "Non-Matching Grant",
            "description": "Something unrelated",
            "tags": ["gaming", "nft"],
            "deadline": "2024-05-10",
            "link": "https://example.com",
            "source": "devfolio",
        },
    ]

    matches = match_project_to_grants(project, grants)
    assert len(matches) == 1
    assert matches[0]["title"] == "Privacy Grant"
    assert matches[0]["score"] > 0
