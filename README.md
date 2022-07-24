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
<p align = 'justify'>Para realizar las descargas del contenido de los enlaces de YouTube se utilizó la librería <a href='https://pytube.io/en/latest/' target="_blank"><code>Pytube</code></a>, que gracias a su facilidad de uso y  continua actualización es una herramienta ideal para trabajar con contenido multimedia.</p> 

### 2. Tkinter
<p align = 'justify'>La GUI fue desarrollada con la ayuda de <a href='https://docs.python.org/es/3/library/tkinter.html'><code>Tkinter</code></a>, una biblioteca gráfica del lenguaje de programación de python, la cual cuenta con un conjunto de herramientas para el desarrollo de interfaces gráficas de usuario.</p>

### 3. OS
<p align = 'justify'>Para realizar la gentión de los archivos descargados (en dónde se guardan, el nombre con el que se guardan, etc.) se utilizó la librería de <a href='https://docs.python.org/3/library/os.html'><code>OS</code></a>, la cual provee al desarrollador de una serie de funcionales propias del sistema operativo de forma protable, como la lectura y escritura de archivos o la manipulación de derectorios.<p>



