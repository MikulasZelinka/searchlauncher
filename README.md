# searchlauncher

Search multiple websites at once using your default browser.

The search (launcher) can be triggered from anywhere as it's listening for a global keypress.

### Installation

```bash
pip install searchlauncher
```

Requires Python 3.11 [for now](#todo).

### Running in background

```bash
searchlauncher
```

to start as a daemon waiting for a [configurable](#settings-and-supported-websites) keypress (e.g., `Ctrl + Shift + E`).

Then type your query and press `Enter` to submit or `Esc` to close the window.

This will open the search for each website in a new tab.

Searching different website groups can be triggered with different hotkeys.

### Searching from console

Instead of running in background, you can use the CLI run a one-off search.

To open a search for all [configured websites](#settings-and-supported-websites):

```shell
searchlauncher search "an item I'm looking for"
```

You can also select a [custom search group](#settings-and-supported-websites):

```shell
searchlauncher search "and now for something completely different" -g en
```

### Settings and supported websites

To open the config file location, you can run

```shell
searchlauncher config
```

after installing.

See the available [`default websites and groups`](src/searchlauncher/settings/default.toml).

You can easily modify this file to add and modify target websites as well as their groups.

You can also customise the default `shortcut` hotkey as well as shortcuts for all groups.

## TODO

- [x] CLI to search for a single item
- [x] GUI (popup on hotkey)
- Configurability
    - [x] Customise the hotkey(s)
    - [x] Customise search sites
    - [x] Customisable search groups
    - [ ] Add and select different browsers
- [ ] Support Python versions older than just 3.11

## Development

### Setup

1. [Install poetry](https://python-poetry.org/docs/#installation) and `cd` to this folder.

2. `poetry install`

3. `poetry run pre-commit install`
