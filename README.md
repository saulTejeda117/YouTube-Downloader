# YouTube Downloader

| Contenido|
| ------------- |
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#-about'><p>About</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#-dependencies'><p>Program Dependencies</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#-configuration'><p>Configuration</p></a>|
| <a href='https://github.com/saulTejeda117/YouTube-Downloader#-how-it-works'><p>How this program works</p></a>|

## 📋 About 
<p align = 'justify'> With this simple desktop application you can download Youtube videos using a simple interface (Fig. 1 Principal Interface).</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.14.43 PM.jpeg"><br>Fig. 1 Principal Interface</img>

## 📰 Dependencies

<p align = 'justify'> This desktop application was developed with programming language, python. The GUI was made with <code>Tkinter</code> package, wich is avaiable on most platforms. <code>Pytube</code>. The ejecutable file <code>youtubeDownloader.exe</code> was created with a very useful application, named <code>AutoPyToExe</code>, with which user can run packaged app without installing Python interpreter or any modules.</p>

```
import tkinter as tk

import os

import pytube
```

<!--Instalation Process -->
## 🛠️ Configuration
> ### 1. Download 'youtubeDownloader.exe' :
<p align='justify'> The first step to use this program is download ejecutable file <code>youtubeDownloader.exe</code>, that you can find in repository's files:</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.03.19 PM.jpeg"><br>Fig. 2 Download ejecutable file</img>

> ### 2. Run it as Administrator
<p align='justify'>When the download ends, run the ejecutable file as administrator:</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.06.59 PM.jpeg"><br>Fig. 3 Run the ejecutable file as administrator</img>

> ### 3. Granting Permits
<p align = 'justify'>Now just granting all the necesary permits (Fig. 4 Granting Permits).</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-24 at 3.42.05 PM.jpeg"><br>Fig. 4 Granting Permits</img>

<!--Instalation Process -->

## 💻 How it works?
> ### 1. Choose a save directory:
<p align='justify'> Choose a save directory using the inrterface buttons (Fig. 5 Choose Save Directory).</p>

<img width="600px" src ="figs/2022-07-24 16-16-14.gif"><br>Fig. 5 Choose Save Directory</img><br>

> ### 2. Add an URL:
<p align='justify'> First add a new youtube link with 'add+' interface button (Fig. 6 Add a Youtube Link), and then it will show all the download links that are content in the download list (Fig. 7 Creation of Download List).</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.28 PM.jpeg"><br>Fig. 6 Add a Youtube Link</img><br>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.13.54 PM.jpeg"><br>Fig. 7 Creation of Download List</img><br>

> ### 3. Download: 
<p align='justify'> When this process ands the application will show a message window.</p>

<img width="250px" src ="figs/WhatsApp Image 2022-07-23 at 11.17.43 PM.jpeg"><br>Fig. 8 Download ends </img><br>
