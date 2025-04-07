# mcp/resources/devfolio.py


def get_devfolio_grants() -> list:
    """Simulated Devfolio grant fetcher."""
    return [
        {
            "title": "Polygon zkEVM Hackathon",
            "description": "Looking for tools, infra, or dApps on Polygon's zkEVM.",
            "tags": ["zkEVM", "Polygon", "hackathon", "infra"],
            "deadline": "2024-04-28",
            "link": "https://devfolio.co/grants/polygon-zkevm",
            "source": "devfolio",
        },
        {
            "title": "Web3 Education Initiative",
            "description": "Funding for projects building open-source Web3 learning platforms.",
            "tags": ["education", "web3", "open-source", "community"],
            "deadline": "2024-05-10",
            "link": "https://devfolio.co/grants/web3-education",
            "source": "devfolio",
        },
    ]
