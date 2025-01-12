import tkinter as tk
from tkinter import ttk
from actions import download
root = tk.Tk()
root.title("AnimeDLapp")
root.geometry("400x400+500+150")

def descargar():
    url = url_input.get()
    start = chapter_i.get()
    end = chapter_f.get()

    if start.isdigit() and end.isdigit():
        start = int(start)
        end = int(end)
        download(url, start, end) 
    else:
        download(url)

welcome = tk.Label(root, text="AnimeFLV Downloader")
welcome.pack(pady=10)

url_section = tk.Frame(root)
url_section.pack(pady=10)

url_label = tk.Label(
    url_section, text="Introduce la url o el titulo de la serie", width=150
)
url_label.pack(pady=10, fill=tk.X)

url_input = tk.Entry(url_section)
url_input.pack(pady=10, fill=tk.X, padx=10)

chapter_selection = tk.Frame(root)
chapter_selection.pack(pady=10)

chapter_i_label = tk.Label(chapter_selection, text="Capitulo inicial")
chapter_i_label.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=10)

chapter_f_label = tk.Label(chapter_selection, text="Capitulo final")
chapter_f_label.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=10)

chapter_selection_entry = tk.Frame(root)
chapter_selection_entry.pack(pady=10)

chapter_i = tk.Entry(chapter_selection_entry)
chapter_i.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=20)

chapter_f = tk.Entry(chapter_selection_entry)
chapter_f.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=20)

botones = tk.Frame(root)
botones.pack(pady=10)

boton_start = tk.Button(botones, text="Descargar", width=20, command=descargar)
boton_start.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=20)

boton_cancel = tk.Button(botones, text="Cancelar", width=20)
boton_cancel.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=20)

progress_label = tk.Label(text="Progreso de descarga")
progress_label.pack(pady=10, fill=tk.X, padx=10)

progress = ttk.Progressbar(root)
progress.pack(pady=10, fill=tk.X, padx=10)

log = tk.Label(bg="white")
log.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

def init():
    root.mainloop()
    
init()