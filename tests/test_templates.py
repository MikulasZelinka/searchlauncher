from multisearch.search import TEMPLATES


def test_templates_have_query():
    assert all("$query" in t for t in TEMPLATES.values())
