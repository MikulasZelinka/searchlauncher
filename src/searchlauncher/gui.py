import platform
from tkinter import Entry, StringVar, Tk

import keyboard
from loguru import logger

from searchlauncher.settings import load_settings

from .search import open_in_browser

SHORTCUT = "ctrl+shift+f"
QUERY_WIDTH = 25
FONT = "Arial 30"

# Our popup window will get focused after this many milliseconds
# FOCUS_DELAY = 42
FOCUS_DELAY = 69
# FOCUS_DELAY = 420


def start_search(query: StringVar, group_name: str | None, root: Tk) -> None:
    query_str: str = query.get()

    # To handle invalid queries:
    # if not(query.startswith('http://') or query.startswith('https://')):
    #     messagebox.showerror("Invalid query", "Must start with http:// or https://")
    #     return

    open_in_browser(query_str, group_name)

    root.destroy()


def show_launcher(group_name: str) -> None:
    root = Tk()
    root.title(f"Search launcher – {group_name}")

    # center on screen
    root.eval("tk::PlaceWindow . center")

    # create the user input for query
    query = StringVar()
    entry = Entry(root, width=QUERY_WIDTH, textvariable=query, font=FONT)
    entry.pack()

    # submit on enter, quit on escape
    root.bind("<Return>", lambda _: start_search(query, group_name, root))
    root.bind("<Escape>", lambda _: root.destroy())

    # move into foreground
    root.attributes("-topmost", True)
    # obtain focus – if the FOCUS_DELAY is too short, root won't get focus (foreground) at all
    root.after(FOCUS_DELAY, lambda: entry.focus_force())

    root.mainloop()


def start_gui() -> None:
    if platform.system() == "Windows":
        logger.debug("Fixing resolution scaling on Windows")
        from ctypes import windll  # type: ignore

        # Fix blurry font with resolution scaling on Windows:
        windll.shcore.SetProcessDpiAwareness(1)

    settings = load_settings()

    for group_name, group in settings.groups.items():

        # a group does not need to have a shortcut, it could just be used by a different group
        if not group.shortcut:
            continue

        logger.info(f"Search {group_name} with '{group.shortcut}'")
        keyboard.add_hotkey(group.shortcut, show_launcher, args=(group_name,))

    # wait() loops automatically:
    keyboard.wait()


if __name__ == "__main__":
    start_gui()
