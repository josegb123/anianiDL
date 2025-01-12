# src/main.py
import fire
from src.anime_actions import download, view_links, search
from src.gui import igui

if __name__ == "__main__":
    fire.Fire(
        {
            "download": download,
            "view-links": view_links,
            "search": search,
            "igui": igui,
        }
    )