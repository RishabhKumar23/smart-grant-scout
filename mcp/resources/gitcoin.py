# mcp/resources/gitcoin.py


def get_gitcoin_grants() -> list:
    """Simulated Gitcoin grant fetcher."""
    return [
        {
            "title": "Layer2 Developer Fund",
            "description": "Support projects building infrastructure on Optimism and Base.",
            "tags": ["Layer2", "SDK", "Optimism", "Base", "tooling"],
            "deadline": "2024-05-15",
            "link": "https://gitcoin.co/grants/layer2-sdk",
            "source": "gitcoin",
        },
        {
            "title": "Decentralized Identity Grant",
            "description": "Grants for self-sovereign identity projects using zk-proofs.",
            "tags": ["identity", "zk", "privacy", "decentralization"],
            "deadline": "2024-06-01",
            "link": "https://gitcoin.co/grants/identity-zk",
            "source": "gitcoin",
        },
    ]
