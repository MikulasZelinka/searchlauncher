import pytest

from searchlauncher.settings import load_settings


@pytest.fixture
def settings():
    return load_settings()


def test_load_default_settings(settings):
    pass


def test_sites_have_query(settings):
    assert all("$query" in x for x in settings.sites.values())


def test_default_group(settings):
    assert "all" in settings.groups
    assert settings.shortcut


def test_groups_only_contain_valid_sites(settings):
    assert all(all(site in settings.sites for site in group.sites) for group in settings.groups.values())


def test_groups_only_contain_valid_groups(settings):
    assert all(all(g in settings.groups for g in group.groups) for group in settings.groups.values())


def test_shortcuts_exist_unique(settings):
    shortcuts = [settings.shortcut] + [group.shortcut for group in settings.groups.values()]
    assert len(shortcuts) == len(set(shortcuts))
