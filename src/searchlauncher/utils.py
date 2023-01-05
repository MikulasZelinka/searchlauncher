from pathlib import Path


def get_project_root() -> Path:
    # this file → this directory == searchlauncher → src → [project_root]
    return Path(__file__).parent.parent.parent.absolute()
