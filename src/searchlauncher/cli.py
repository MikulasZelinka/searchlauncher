from typing import Optional

import typer

from searchlauncher import open_in_browser, start_gui


def cli(query: Optional[str] = typer.Argument(None)) -> None:
    """
    Starts a daemon listening for a keyboard shortcut,
    unless query is specified – in which case, it opens search for the query.

    Args:
        query:

    Returns:

    """
    if query:
        open_in_browser(query)
    else:
        start_gui()


def main() -> None:
    # we wrap cli() inside main() so that typer runs even when main() is invoked directly
    typer.run(cli)


if __name__ == "__main__":
    main()
