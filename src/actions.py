# src/anime_actions.py
from scrapper import scrap_one, search_anime
from downloader import download_one, showlinks

def view_links(
    title: str,
    start: int = 1,
    end: int = 1,
    output_path: str = ".",
    override: bool = True,
):
    links = []
    for chapter in range(start, end + 1):
        links.append(
            scrap_one(
                title, chapter=chapter, output_path=output_path, override=override
            )
        )
    showlinks(links)

def download(
    title: str,
    start: int = 1,
    end: int = 1,
    output_path: str = ".",
    override: bool = False,
):
    links = []
    for chapter in range(start, end + 1):
        links.append(
            scrap_one(
                title, chapter=chapter, output_path=output_path, override=override
            )
        )
    download_one(links)

def search(
    query: str,
    download_all: bool = False,
    output_path: str = ".",
    override: bool = False,
):
    results = search_anime(query)

    for title, (url, chapters) in results.items():
        print(title, f"[{chapters} chapters]", f"( {url} )")

    if download_all:
        for title, (url, chapters) in results.items():
            view_links(
                url, start=1, end=chapters, output_path=output_path, override=override
            )