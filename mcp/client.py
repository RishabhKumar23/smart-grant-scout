# mcp/client.py

from mcp.resources.gitcoin import get_gitcoin_grants
from mcp.resources.devfolio import get_devfolio_grants


def get_all_grants() -> list:
    """Aggregate and normalize grants from all sources."""
    gitcoin = get_gitcoin_grants()
    devfolio = get_devfolio_grants()
    return gitcoin + devfolio
