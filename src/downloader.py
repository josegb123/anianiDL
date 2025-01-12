import json
import os
import time
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_downloads(download_path):
    while True:
        if any([filename.endswith('.fdmdownload') for filename in os.listdir(download_path)]):
            time.sleep(1)  # Esperar un segundo antes de volver a comprobar
        else:
            break

def download_one(links):
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "D:\\"}
    options.add_experimental_option("prefs", prefs)
    fdm_path = "C:\\Program Files\\Softdeluxe\\Free Download Manager"
    if os.path.exists(fdm_path):
        print("FDM está instalado.")
    
        # Construye la ruta del archivo .crx
        extension_path = os.path.join(os.getcwd(), "src\\fdm.crx")  # Asumiendo que el archivo está en la misma carpeta que el script

        # Verifica si el archivo .crx existe
        if os.path.exists(extension_path):
            try:
                options.add_extension(extension_path)
                print("Extensión agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar la extensión: {e}")
            else:
                print("El archivo de extensión no se encontró. Continuando con el programa...")
    else:
        print("La carpeta de FDM no se encontró. Continuando con el programa...")
            
    options.page_load_strategy = 'eager'
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    for url in links:
        url = url.strip()  # Eliminar espacios en blanco
        driver.get(url)
        # Hacer clic en el botón tan pronto como esté disponible
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "download"))).click()
            time.sleep(10)
            # Esperar a que la descarga se complete
            wait_for_downloads('D:\\Descargas')

        except Exception as e:
            print(f'Error al procesar {url}: {e}')
        
    driver.quit()
        
def download_one_file(link):
    print("Looking for GoCDN link")
    html = requests.get(link).text
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

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "D:\\"}
    options.add_experimental_option("prefs", prefs)
    fdm_path = "C:\\Program Files\\Softdeluxe\\Free Download Manager"
    if os.path.exists(fdm_path):
        print("FDM está instalado.")
    
        # Construye la ruta del archivo .crx
        extension_path = os.path.join(os.getcwd(), "src\\fdm.crx")  # Asumiendo que el archivo está en la misma carpeta que el script

        # Verifica si el archivo .crx existe
        if os.path.exists(extension_path):
            try:
                options.add_extension(extension_path)
                print("Extensión agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar la extensión: {e}")            
    else:
        print("La carpeta de FDM no se encontró. Continuando con el programa...")
            
    options.page_load_strategy = 'eager'
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    
    url = url.strip()  # Eliminar espacios en blanco
    driver.get(url)
    # Hacer clic en el botón tan pronto como esté disponible
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "download"))).click()
        time.sleep(10)
        # Esperar a que la descarga se complete
        wait_for_downloads('D:\\Descargas')

    except Exception as e:
        print(f'Error al procesar {url}: {e}')
    
    driver.quit()
        
def showlinks(links):
    for link in links:
        print(link)