import json
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from downloader import download_one_file as download
from scrapper import cargar_animes

def cargar_datos():
    try:
        cargar_animes()        
        with open('animes.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo animes.json no se encontró.")
        return []

def mostrar_seleccionados():
    seleccionados = []
    for anime in checkboxes:
        if anime['var'].get():  # Si el checkbox está seleccionado
            seleccionados.append(anime['titulo'])  # Acceder al título
    messagebox.showinfo("Capítulos Seleccionados", "\n".join(seleccionados) if seleccionados else "No se ha seleccionado ningún capítulo.")

def descargar_seleccionados():
    for anime in checkboxes:
        if anime['var'].get():  # Si el checkbox está seleccionado
            link = anime['url']
            capitulo_str = anime['capitulo']  # Obtener el capítulo como cadena            
            download(link)  # Llamar a la función de descarga

style = Style()

root = style.master
root.title("Seleccionar Capítulos de Anime")

# Cargar los datos
animes_data = cargar_datos()

# Lista para almacenar los checkboxes
checkboxes = []

# Crear checkboxes para cada anime
for anime in animes_data:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=f"{anime['titulo']} - {anime['capitulo']}", variable=var)
    checkbox.pack(anchor='w')
    checkboxes.append({'titulo': anime['titulo'], 'capitulo': anime['capitulo'], 'url': anime['url'], 'var': var})  # Almacenar título, capítulo, URL y variable

# Botón para mostrar los capítulos seleccionados
boton_mostrar = tk.Button(root, text="Mostrar Seleccionados", command=mostrar_seleccionados)
boton_mostrar.pack(side=tk.LEFT, padx=10,pady=10,expand=True)

# Botón para descargar los capítulos seleccionados
boton_descargar = tk.Button(root, text="Descargar Seleccionados", command=descargar_seleccionados)
boton_descargar.pack(side=tk.LEFT, padx=10,pady=10,expand=True)

# Iniciar el bucle principal de la interfaz
root.mainloop()