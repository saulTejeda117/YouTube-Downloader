# YouTube Downloader

| Contenido|
| ------------- |
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#About'><p>About</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#Dependencies'><p>Program Dependencies</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#Instalación'><p>Program Instalation</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#funcionamiento'><p>How it works</p></a>|

## About 
<p align = 'justify'> With this simple desktop application you can download Youtube videos using a simple interface (Fig. 1 Principal Interface).</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.14.43 PM.jpeg"><br>Fig. 1 Principal Interface</img>

## Dependencies
<p align = 'justify'> Para la elaboración de este pequño programa se hizo uso de una serie librerías especificas del lenguaje de programación de python, así como un programa de creación de archivos ejecutables de windows para la creación del archivo <code>youtubeDownloader.exe</code>. <code>Tkinter</code>, <code>Pytube</code>, <code>OS</code> and <code>AutoPyToExe</code> Las librerías utilizadas para la elaboración del trbajo se encuentran en a continuación:</p>

```
import tkinter as tk

import os

import pytube
```
<!--
> ### 1. Pytube
<p align = 'justify'>Para realizar las descargas del contenido de los enlaces de YouTube se utilizó la librería <a href='https://pytube.io/en/latest/' target="_blank"><code>Pytube</code></a>, que gracias a su facilidad de uso y  continua actualización es una herramienta ideal para trabajar con contenido multimedia. A continuación, se muestra el uso de una de las funciones de esta librería dentro de la función de descarga y guardado de videos, dentro del código<code>youtubeDownloader.py</code>:</p>

> ### 2. Tkinter
<p align = 'justify'>La GUI fue desarrollada con la ayuda de <a href='https://docs.python.org/es/3/library/tkinter.html'><code>Tkinter</code></a>, una biblioteca gráfica del lenguaje de programación de python, la cual cuenta con un conjunto de herramientas para el desarrollo de interfaces gráficas de usuario. El código siguiente muestra un poco del uso de esta librería dentro de la función principal:</p>

> ### 3. OS
<p align = 'justify'>Para realizar la gentión de los archivos descargados (en dónde se guardan, el nombre con el que se guardan, etc.) se utilizó la librería de <a href='https://docs.python.org/3/library/os.html'><code>OS</code></a>, la cual provee al desarrollador de una serie de funcionales propias del sistema operativo de forma protable, como la lectura y escritura de archivos o la manipulación de derectorios.</p>

> ### 4. AutoPyToExe
<p align='justify'><a href='https://pyinstaller.org/en/stable/'><code>Auto PY to EXE</code></a> es una librería especial del lenguaje de programación de Python, a través del cual es posible convertir una archivo '.py' en un archivo executable '.exe', junto con todas sus dependencias.</p>

-->

<!--Instalation Process -->
## Program Instalation
> ### 1. Download 'youtubeDownloader.exe' :
<p align='justify'> The first step to use this program is download ejecutable file <code>youtubeDownloader.exe</code>, that you can find in repository's files:</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.03.19 PM.jpeg"><br>Fig. 2 Download ejecutable file</img>

> ### 2. Run it as Administrator
<p align='justify'>When the download ends, run the ejecutable file as administrator:</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.06.59 PM.jpeg"><br>Fig. 3 Run the ejecutable file as administrator</img>

> ### 3. Granting Permits
<p align = 'justify'>Now just granting all the necesary permits:</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.42.05 PM.jpeg"><br>Fig. 4 Granting Permits</img>

<!--Instalation Process -->
## How it works?
> ### 1. Choose a save directory:
<p align='justify'>Una vez dentro de la interfaz principal de usuario podremos utilizar los botones dentro, para seleccionar la carpeta de guardado de arcchivos.</p>

<img width="600px" src ="figs/2022-07-24 16-16-14.gif"><br>Fig. 5 Escoger Directorio de Guardado</img><br>

> ### 2. Add an URL:
<p align='justify'> Posteriormente, dentro del segundo cuadro de texto pagaremos el link de descarga del video que deseamos descargar y damos click en el botón de agregar a la lista de descargas (Fig. 7 Ingresar Link de Descarga a la Lista), una vez hecho esto la lista se desplegará al final de la interfaz (Fig. 8 Añadir Link de Descarga a la Lista).</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.28 PM.jpeg"><br>Fig. 8 Add a Youtube Link</img><br>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.54 PM.jpeg"><br>Fig. 9 Creation of Download List</img><br>

> ### 3. Download: 
<p align='justify'> Al final sólo es necesario presionar el botón de iniciar descarga y comenzará el proceso automáticamente. Por último, al terminar las descargas se desplegará un mensaje, indicando que el proceso de descarga ha concluido.</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.17.43 PM.jpeg"><br>Fig. 10 Descargas Concluidas</img><br>
