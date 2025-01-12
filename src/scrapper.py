import requests
import bs4
import re
import json
from tqdm import tqdm
from pathlib import Path


def search_anime(query: str, find_details: bool = True):
    print(f"Searching query: {query}")
    url = f"https://www3.animeflv.net/browse?q={query}"
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, features="html.parser")

    items = soup.find("ul", {'class': 'ListAnimes'}).find_all('li')
    results = {}

    for item in tqdm(items, desc="Looking up details", unit=' title'):
        title = item.find("h3", {'class': 'Title'}).text
        item_url = item.find('a').attrs['href'].replace('/anime/', "")

        if find_details:
            item_html = requests.get(f"https://www3.animeflv.net/anime/{item_url}").text
            anime_details = re.search(r"var episodes = (?P<list_items>\[.+]);", item_html).groups('list_items')[0]
            total_chapters = json.loads(anime_details)[0][0]  # Cambiado a json.loads
        else:
            total_chapters = None

        results[title] = (item_url, total_chapters)

    return results

def find_details(anime_id: str):
    item_html = requests.get(f"https://www3.animeflv.net/anime/{anime_id}").text
    anime_details = re.search(r"var episodes = (?P<list_items>\[.+]);", item_html).groups('list_items')[0]
    description = bs4.BeautifulSoup(item_html, features="html.parser").find("div", {'class': 'Description'}).text
    total_chapters = json.loads(anime_details)[0][0]  # Cambiado a json.loads

    return total_chapters, description

def showlinks(links):
    for link in links:
        print(link)


def scrap_one(title: str, chapter: int, output_path: str, return_url: bool = False, override: bool = False):

    print(f" Downloading {title}-{chapter}")

    path = Path(output_path) / f"{title}"

    if path.exists():
        if not override:
            print("(!) Refusing to override. Pass override=True (--override in the CLI) to force.")
            return

    print("Downloading AnimeFLV.net webpage")
    html = requests.get(f"https://www3.animeflv.net/ver/{title}-{chapter}").text

    print("Looking for GoCDN link")

    soup = bs4.BeautifulSoup(html, features="html.parser")
    lines = str(soup).split("\n")

    for l in lines:
        if l.strip().startswith("var videos = {"):
            break

    l = l.strip()
    data = json.loads(l[13:-1])
    for d in data["SUB"]:
        if d["server"] == "yu":
            break

    url = d["code"].replace("embed","watch")

    print("Found YourUpload url")
    return url

def cargar_animes():
        url = "https://www3.animeflv.net/"
            
        response = requests.get(url).text

        # Crear un objeto BeautifulSoup
        soup = bs4.BeautifulSoup(response, 'html.parser')  # Puedes usar 'html.parser' si lo prefieres

        # Encontrar todos los elementos <li>
        li_elements = soup.find_all("li")

        # Lista para almacenar los datos de los animes
        animes_data = []

        # Base URL
        base_url = "https://www3.animeflv.net"

        for li in li_elements:
            a_tag = li.find("a")  # Encontrar el <a> dentro del <li>
            strong = li.find("strong", class_="Title")  # Encontrar el <strong> con la clase 'Title'
            span = li.find("span", class_="Capi")

            if a_tag and strong:
                title = strong.text.strip()  # Obtener el texto del <strong> como título
                relative_url = a_tag['href']  # Obtener el atributo href (URL)
                url = base_url + relative_url  # Convertir a URL absoluta
                capitulo = span.text.strip() if span else "N/A"  # Manejar el caso donde no hay <span>

                # Crear un diccionario para el anime
                anime_info = {
                    "titulo": title,
                    "capitulo": capitulo,  # Aquí puedes agregar lógica para obtener el capítulo si está disponible
                    "url": url
                }
                
                # Agregar el diccionario a la lista
                animes_data.append(anime_info)

        # Convertir la lista a JSON
        animes_json = json.dumps(animes_data, ensure_ascii=False, indent=4)

        # Guardar el JSON en un archivo
        with open('animes.json', 'w', encoding='utf-8') as json_file:
            json_file.write(animes_json)

        print("Los datos de los animes han sido guardados en animes.json")