# anianiDL
AnimeFLV scrapper y downloader, basado en el proyecto https://github.com/apiad/animeflv-downloader?tab=readme-ov-file

#FDM opcional
Para poder usarse se necesita tener FDM instalado(https://www.freedownloadmanager.org/es/download.htm), ya que el servidor YU no acepta la descarga automatizada, ademas en su configuracion debemos marcar "agregar descarga sin confirmar", para que el proceso se automatize por completo

#Dependencias
```python
pip install -r requeriments.txt
```

#Uso
##Descargar
puedes usarlo desde linea de comandos usando como directorio de trabajo src, por ejemplo:
de este enlace: https://www3.animeflv.net/anime/srank-monster-no-behemoth-dakedo-neko-to-machigawarete-elf-musume-no-pet-toshite-kurashitemasu
solo usaremos el titulo url: srank-monster-no-behemoth-dakedo-neko-to-machigawarete-elf-musume-no-pet-toshite-kurashitemasu
en el siguiente ejemplo descargaremos desde el capitulo 1 hasta el 3, si no agregamos el capitulo, por defecto solo descarga el primero
Nota: Las descargas se guardan en la ruta por defecto de descargas si no se tiene FDM para especificarlas

```pyhon
python -m main.py download srank-monster-no-behemoth-dakedo-neko-to-machigawarete-elf-musume-no-pet-toshite-kurashitemasu 1 3
```
##Buscar
```pyhon
python -m main.py download srank-monster-no-behemoth-dakedo-neko-to-machigawarete-elf-musume-no-pet-toshite-kurashitemasu 1 3
```

##GUI
hay dos Interfaces, una para descargar una serie o un capitulo(gui.py) y una para descargar los ultimos capitulos(gui_json.py)

```pyhon
python -m gui.py
```

```pyhon
python -m gui_json.py
```

#TO-DO list
- [x] Funcional
- [x] Acrapper para ultimos capitulos
- [x] GUI(40%)
- [ ] Estructurar a POO
- [ ] Limpiar codigo
- [ ] Barra de progreso
- [ ] Agregar base de datos para series decargadas
- [ ] Resolver bugs
