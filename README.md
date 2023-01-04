# searchlauncher

Open a web search using your default browser with multiple search providers at once.

### Installation

`pip install searchlauncher`

Once installed, restart your shell so that `searchlauncher` works.

### Running in background

Run

```
searchlauncher
```

to start as a daemon waiting for a keypress (`CTRL + SHIFT + F`).

Then type your query and press `Enter` to submit or `Esc` to close the window.

### One-off search

```shell
searchlauncher "an item I'm looking for"
```

### Supported websites

For now, see the available [`TEMPLATES`](src/searchlauncher/search.py).

## TODO

- [x] CLI to search for a single item
- [x] GUI (popup on hotkey)
- Configurability
    - [ ] Customise the hotkey
    - [ ] Add and select search providers
    - [ ] Add and select different browsers
- GUI
    - [ ] Provider groups

## Development

### Setup

1. [Install poetry](https://python-poetry.org/docs/#installation) and `cd` to this folder.

2. `poetry install`

3. `poetry run pre-commit install`
