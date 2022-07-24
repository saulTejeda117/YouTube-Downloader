# Youtube music downloader
from queue import Empty
import tkinter as tk

from tkinter import *

import os
from tkinter import filedialog, messagebox
from turtle import onclick

import pytube

# Creation of downLoad list elements
downloadList = []
username = os.getlogin( ) 
def addQueueURL(mainWindow, urlPath):
    global downloadList
    global saveDirectory
    # Check if URL is empty
    if(urlPath == ''):
        messagebox.showinfo(message = "Error: Ninguno de los Campos Puede Estar Vacio, Por Favor Intentelo De Nuevo", title = "Error")
    else:
        saveDirectory = 'C:/Users/' + username + '/Music'
        urlpath = urlPath.split('♫z2!3ð')
        downloadList = downloadList + urlpath
        resfresh(mainWindow)

# Refresh the mainWindow with new info 
# -> Save Directory
# -> Updated download list
def resfresh(mainWindow):
    mainWindow.destroy()
    main(saveDirectory)

# Definition of save directory path function
def getSaveDirectoryPath(mainWindow):
    global saveDirectory
    cwd = filedialog.askdirectory()
    saveDirectory = cwd
    resfresh(mainWindow)

# Download-Save function
def saveVideo(videoDirection):
    global saveDirectory
    file = videoDirection.streams.filter(only_audio=True).first()
    outputFile = file.download(saveDirectory)
    base, ext = os.path.splitext(outputFile)
    # It'll save as mp3
    new_file = base + '.mp3'
    fileExists = os.path.exists(new_file)
    print(fileExists)
    # If file allready exists it'll be renamed
    if(fileExists == True):
        x = 1
        while(fileExists == True):
            print('Si llega' )
            repit = base + str(x) + '.mp3'
            fileExists = os.path.exists(repit)
            print(repit)
            x += 1 
        os.rename(new_file, repit)
    else:
        os.rename(outputFile, new_file)
        # Confirmation
        print('Descarga Terminada: ', file)

def startDownload(mainWindow):
    global downloadList
    global saveDirectory
    saveDirectory = 'C:/Users/' + username + '/Music'
    for x in downloadList:
            print(x)
            yt = pytube.YouTube(x)  
            saveVideo(yt)
    messagebox.showinfo(message = "Se Han Concluido las Descargas", title = "Descarga Terminada")
    downloadList = []
    print('Lista Vacia: ', downloadList)
    resfresh(mainWindow)

def main(defaultSaveDirectoryPath):
    global downloadList
    saveDirectory = ""
    # Main window object declaration
    mainWindow = tk.Tk()

    # Principal Elements of mainWindow
    mainWindow.title("YouTube Downloader")
    mainWindow.config(width = 400, height = 300)
    mainWindow.resizable(False, False)
    tk.Label(text = 'YouTube Videos Downloader').place(x = 125, y = 20)

    # Get SaveDirectory 
    tk.Label(text = 'Save Directory: ').place(x = 50, y = 60)
    saveDirectoryPath = tk.Entry(mainWindow, width = 30)
    directoryPath = saveDirectoryPath.get()
    saveDirectoryPath.insert(0, defaultSaveDirectoryPath)
    saveDirectoryPath.config(state = 'disabled')

    # Choose where to save the videos
    buttonSaveDirectoryPath = tk.Button(text = 'Add +') #, command = lambda: getSaveDirectoryPath(mainWindow))

    # Get the YouTube URL
    tk.Label(text = 'YouTube URL: ').place(x = 50, y = 100)
    text = tk.StringVar()
    url = tk.Entry(mainWindow, textvariable = text, width = 30)
    addQueueButton = tk.Button(text = 'Add +', command = lambda: addQueueURL(mainWindow, url.get()))  

    # Start the download
    tk.Button(text = ' Start ►', command = lambda: startDownload(mainWindow)).place(x = 150, y = 140)

    t = tk.Text(mainWindow, width = 35, height = 5)
    if(len(downloadList) > 0):
        for x in downloadList:
            t.insert(END, x + '\n\n')
        t.config(state='disabled')
        t.place(x = 50, y = 180)
        
    # Some elements positions
    buttonSaveDirectoryPath.place(x = 335, y = 55)
    saveDirectoryPath.place(x = 145, y = 60)
    addQueueButton.place(x = 335, y = 95)
    url.place(x = 145, y = 100)

    # Show the main window function
    mainWindow.mainloop()
main('C:/Users/' + username + '/Music')