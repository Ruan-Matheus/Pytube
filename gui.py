from tkinter import *
from tkinter import filedialog
import youtube
import playlist
import re


def browser():
    path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, path)
    return path


def download():
    diretorio = path.get()
    link = url.get()
    
    if not link or not diretorio:
        return

    regex_video = re.compile(r"https:\/\/www\.youtube\.com\/watch\?v=")
    regex_playlist = re.compile(r"https:\/\/www\.youtube\.com/playlist\?list=")


    if (regex_video.findall(link)):
        youtube.downlaod_youtube(link, diretorio, hd=True)

    elif (regex_playlist.findall(link)):
        playlist.download_playlist(diretorio, link, mp3=False, hd=True)

    # Link invalido
    return


window = Tk() # Instatiate an instace of a window
window.title("YouTube Video Downloader")
window.geometry("700x200")
window.config(background= 'white')
window.resizable(False, False)

icon = PhotoImage(file = 'img.png')
window.iconphoto(True, icon)

url = StringVar()
path = StringVar()


# URL
url_label = Label(window, 
            text="URL:   ",
            font= ("Ariel", 10, 'bold'),
            bd= 5,
            padx= 5,
            height= 1)
url_label.place(x= 5, y = 10)

url_entry = Entry(window, font=("Ariel", 10, "normal"), textvariable=url)
url_entry.place(x = 100, y = 20, width=470, height=20)
url_entry.focus()

# DIRETORIO
path_label = Label(window,
                 text="PATH: ",
                 font=("Ariel", 10, 'bold'),
                 bd = 5,
                 padx= 5)
path_label.place(x = 5, y = 50)

path_entry = Entry(window,
                   font=("Ariel", 10, "normal"),
                   #border= 20,
                   textvariable= path)
path_entry.place(x = 100, y = 60, width=470, height=20)



searchButton = Button(window,
                      text = "Search",
                      font=("Ariel", 10, 'normal'),
                      padx= 10,
                      command= browser)
searchButton.place(x = 600, y = 55)


downloadButton = Button(window, text= "Download", command= download)
downloadButton.place(x=300, y=150)





window.mainloop()