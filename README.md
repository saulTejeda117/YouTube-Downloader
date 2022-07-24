# YouTube Video Downloader With GUI

<p align = 'justify'>Con esta sencilla aplicación de escritorio es posible descargar un sin fin de archivos de audio y video directamente de un enlace de YouTube. A través de su interfaz gráfica de usuario (fig. 1 Interfaz Principal) y los diferentes botones propios de dicha interfaz, es posible crear una lista de descarga de forma sencilla (fig. 2 Lista de Descargas), así como la configuración de la ruta de almacenamiento dentro de nuestro equipo, de esta manera realizar las descargas de forma casi instantanea, todo esto de forma portable, fácil y segura, todo esto sin la necesidad de pagar por algún servicio de suscripción, como el que ofrece YouTube, pudiendo acceder al contenido que se desea, cuando se desea.</p>

> <img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.11.31 PM.jpeg"><br>Fig. 1 Interfaz Principal</img><br>
> <img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.14.43 PM.jpeg"><br>Fig. 2 Lista de Descargas</img><br>

## Librerias y Recursos Utilizados
Para la elaboración de este pequño programa se hizo uso de una serie librerías especificas del lenguaje de programación de python, así como un programa de creación de archivos ejecutables de windows para la creación del archivo `youtubeDownloader.exe`

```
import tkinter as tk

from tkinter import *

import os
from tkinter import filedialog, messagebox

import pytube
```
