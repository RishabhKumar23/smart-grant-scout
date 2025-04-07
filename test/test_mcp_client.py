# tests/test_mcp_client.py

from mcp.client import get_all_grants


def test_grants_not_empty():
    grants = get_all_grants()
    assert isinstance(grants, list)
    assert len(grants) > 0


def test_grant_fields():
    grants = get_all_grants()
    required_fields = {"title", "description", "tags", "deadline", "link", "source"}
    for grant in grants:
        assert required_fields.issubset(grant.keys())
