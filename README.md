# YouTube Video Downloader With GUI

<p align = 'justify'>Con esta sencilla aplicación de escritorio es posible descargar un sin fin de archivos de audio y video directamente de un enlace de YouTube. A través de su interfaz gráfica de usuario (fig. 1 Interfaz Principal) y los diferentes botones propios de dicha interfaz, es posible crear una lista de descarga de forma sencilla (fig. 2 Lista de Descargas), así como la configuración de la ruta de almacenamiento dentro de nuestro equipo, de esta manera realizar las descargas de forma casi instantanea, todo esto de forma portable, fácil y segura, todo esto sin la necesidad de pagar por algún servicio de suscripción, como el que ofrece YouTube, pudiendo acceder al contenido que se desea, cuando se desea.</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.11.31 PM.jpeg"><br>Fig. 1 Interfaz Principal</img><br>
<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.14.43 PM.jpeg"><br>Fig. 2 Lista de Descargas</img><br>

## Librerías y Recursos Utilizados
<p align = 'justify'> Para la elaboración de este pequño programa se hizo uso de una serie librerías especificas del lenguaje de programación de python, así como un programa de creación de archivos ejecutables de windows para la creación del archivo <code>youtubeDownloader.exe</code>. Las librerías utilizadas para la elaboración del trbajo se encuentran en a continuación:</p>

```
import tkinter as tk
from tkinter import *

import os
from tkinter import filedialog, messagebox

import pytube
```

### 1. Pytube
<p align = 'justify'>Para realizar las descargas del contenido de los enlaces de YouTube se utilizó la librería <a href='https://pytube.io/en/latest/' target="_blank"><code>Pytube</code></a>, que gracias a su facilidad de uso y  continua actualización es una herramienta ideal para trabajar con contenido multimedia. A continuación, se muestra el uso de una de las funciones de esta librería dentro de la función de descarga y guardado de videos, dentro del código <a href='https://github.com/saulTejeda117/YouTube-Video-Downloader/blob/main/youtubeDownloader.py' target="_blank"><code>youtubeDownloader.py</code></a>:</p>

```
# Download-Save function
def saveVideo(videoDirection):
    global saveDirectory
    file = videoDirection.streams.filter(only_audio=True).first()
    outputFile = file.download(saveDirectory)
    (...)
    
```

### 2. Tkinter
<p align = 'justify'>La GUI fue desarrollada con la ayuda de <a href='https://docs.python.org/es/3/library/tkinter.html'><code>Tkinter</code></a>, una biblioteca gráfica del lenguaje de programación de python, la cual cuenta con un conjunto de herramientas para el desarrollo de interfaces gráficas de usuario. El código siguiente muestra un poco del uso de esta librería dentro de la función principal:</p>

```
def main(defaultSaveDirectoryPath):
    global downloadList
    saveDirectory = ""
    # Main window object declaration
    mainWindow = tk.Tk()

    # Principal mainWindow Elements
    mainWindow.title("YouTube Downloader")
    mainWindow.config(width = 400, height = 300)
    mainWindow.resizable(False, False)
    tk.Label(text = 'YouTube Videos Downloader').place(x = 125, y = 20)
    
    # More Elements 
    (...)
    
    mainWindow.mainloop()  
main('C:/Users/' + username + '/Music')
```

### 3. OS
<p align = 'justify'>Para realizar la gentión de los archivos descargados (en dónde se guardan, el nombre con el que se guardan, etc.) se utilizó la librería de <a href='https://docs.python.org/3/library/os.html'><code>OS</code></a>, la cual provee al desarrollador de una serie de funcionales propias del sistema operativo de forma protable, como la lectura y escritura de archivos o la manipulación de derectorios.</p>

```
username = os.getlogin( )

(...)

def saveVideo(videoDirection):
    global saveDirectory
    file = videoDirection.streams.filter(only_audio=True).first()
    outputFile = file.download(saveDirectory)
    base, ext = os.path.splitext(outputFile)
    
    # It'll save as mp3
    new_file = base + '.mp3'
    fileExists = os.path.exists(new_file)
    
(...)

```

### 4. AutoPyToExe
<p align='justify'><a href='https://pyinstaller.org/en/stable/'><code>Auto PY to EXE</code></a> es una librería especial del lenguaje de programación de Python, a través del cual es posible convertir una archivo '.py' en un archivo executable '.exe', junto con todas sus dependencias.</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.26.07 PM.jpeg">Fig. 3 Interfaz de Auto PY to EXE</img><br>

## Funcionamiento
### 1. Descargar Achivo 'youtubeDownloader.exe' 
<p align='justify'> Dentro del repositorio es posible encontrar la versión ejecutable del código con el nombre de <code>youtubeDownloader.exe</code>, entonces descargaremos el archivo ejecutable desde el repositorio.</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.03.19 PM.jpeg">Fig. 4 Descargar Archivo Ejecutable</img><br>

### 2. Ejecutartalo como Administrador
<p align='justify'> Accederemos a la carpeta dónde se encuentra el archivo ejecutable y procederemos a ejecutarlo como administrador.</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.06.59 PM.jpeg">Fig. 5 Escoger Directorio de Guardado</img><br>

### 3. Conceder los permisos necesarios
<p align = 'justify'>Posteriormente concederemos los permisos necesarios en la ventana de windows que aparecerá.</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.42.05 PM.jpeg">Fig. 6 Conceder los Permisos</img><br>

### 4. Escoger el Directorio Dónde se Guardar las Descargas
<p align='justify'>Una vez dentro de la interfaz principal de usuario podremos utilizar los botones dentro, para seleccionar la carpeta de guardado de arcchivos.</p>
<img width="250px" src ="figs/2022-07-24 16-16-14.gif">Fig. 7 Escoger Directorio de Guardado</img><br>

### 5. Añadir links de Descarga 
<p align='justify'> Posteriormente, dentro del segundo cuadro de texto pagaremos el link de descarga del video que deseamos descargar y damos click en el botón de agregar a la lista de descargas (Fig. 7 Ingresar Link de Descarga a la Lista), una vez hecho esto la lista se desplegará al final de la interfaz (Fig. 8 Añadir Link de Descarga a la Lista).</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.28 PM.jpeg">Fig. 8 Ingresar Link De Descarga</img><br>
<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.54 PM.jpeg">Fig. 9 Añadir Link De Descarga a la Lista</img><br>

### 6. Comenzar Descarga 
<p align='justify'> Al final sólo es necesario presionar el botón de iniciar descarga y comenzará el proceso automáticamente. Por último, al terminar las descargas se desplegará un mensaje, indicando que el proceso de descarga ha concluido.</p>
<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.17.43 PM.jpeg">Fig. 9 Iniciar Descarga</img><br>

## Referencias


