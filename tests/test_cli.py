from typer.testing import CliRunner

from searchlauncher.cli import cli

runner = CliRunner()


# TODO: how to test without actually opening webbrowser?
def test_search_cli_default():
    result = runner.invoke(cli, ["search", "Lenovo Yoga 7 14ARB7"])
    assert result.exit_code == 0


# TODO: how to test without actually opening webbrowser?
def test_search_cli_group():
    result = runner.invoke(cli, ["search", "Lenovo Yoga 7 14ARB7", "-g", "custom"])
    assert result.exit_code == 0


# TODO: how to test without actually opening file browser?
def test_config_cli():
    result = runner.invoke(cli, ["config"])
    assert result.exit_code == 0


# # TODO: how to test (this would hang indefinitely)?
# def test_gui_cli():
#     result = runner.invoke(cli, [])
#     assert result.exit_code == 0
