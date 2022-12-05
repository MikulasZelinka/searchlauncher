import platform
from tkinter import Entry, StringVar, Tk

import keyboard
from loguru import logger

from .search import open_in_browser

SHORTCUT = "ctrl+shift+f"
QUERY_WIDTH = 25
FONT = "Arial 30"

# Our popup window will get focused after this many milliseconds
FOCUS_DELAY = 42


def start_search(query: StringVar, root: Tk) -> None:
    query_str: str = query.get()

    # To handle invalid queries:
    # if not(query.startswith('http://') or query.startswith('https://')):
    #     messagebox.showerror("Invalid query", "Must start with http:// or https://")
    #     return

    open_in_browser(query_str)

    root.destroy()


def show_popup() -> None:
    root = Tk()
    root.title("Multisearch")

    # center on screen
    root.eval("tk::PlaceWindow . center")

    # create the user input for query
    query = StringVar()
    entry = Entry(root, width=QUERY_WIDTH, textvariable=query, font=FONT)
    entry.pack()

    # submit on enter, quit on escape
    root.bind("<Return>", lambda _: start_search(query, root))
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

    logger.info(f"Starting in background, activate the search by using '{SHORTCUT}'")
    keyboard.add_hotkey(SHORTCUT, show_popup)
    # wait() loops automatically:
    keyboard.wait()


if __name__ == "__main__":
    start_gui()
