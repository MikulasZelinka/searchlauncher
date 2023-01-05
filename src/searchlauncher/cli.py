from enum import StrEnum
from typing import Generator

import typer
from loguru import logger

from searchlauncher import open_in_browser, start_gui
from searchlauncher.settings import DEFAULT_SETTINGS_PATH, load_settings

cli = typer.Typer()

settings = load_settings()
Group = StrEnum("Group", list(settings.groups.keys()))  # type: ignore


def complete_groups(incomplete: str) -> Generator[tuple[str, str], None, None]:
    for group_name, group in settings.groups.items():
        if group_name.startswith(incomplete):
            yield group_name, ", ".join(group.sites)


@cli.command()
def search(
    query: str,
    group: Group = typer.Option(  # type: ignore
        None,
        "--group",
        "-g",
        autocompletion=complete_groups,
        case_sensitive=False,
    ),
) -> None:
    """
    Directly open search for the given query using all sites or the specified group.

    Searches all sites unless a group is specified with "-g" or "--group" (see "searchlauncher config").
    """
    open_in_browser(query, group_name=group)


@cli.command()
def config() -> None:
    """
    Open the config directory.

    You can modify the "toml" file to modify keyboard shortcuts, sites and groups.
    """
    settings_dir = str(DEFAULT_SETTINGS_PATH)
    logger.info(f"Opening settings directory: {settings_dir}")
    typer.launch(settings_dir, locate=True)


@cli.callback(invoke_without_command=True)
def run(
    ctx: typer.Context,
) -> None:
    """
    Run search launcher in background, waiting for shortcuts.

    See the "Commands" section below for more.
    """

    # This makes running just "searchlauncher" without any further commands run the main loop
    # https://github.com/tiangolo/typer/issues/18
    if ctx.invoked_subcommand is not None:
        # If there's any command, we don't run the main loop
        return
    start_gui()


if __name__ == "__main__":
    cli()
