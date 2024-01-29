from tkinter import *
from tkinter import filedialog
import youtube


def browser():
    path = filedialog.askdirectory()
    #path_entry.clear # or something loke this
    path_entry.insert(0, path)
    return path


def download():
    diretorio = path.get()
    link = url.get()
    youtube.downlaod_youtube(link, diretorio)


window = Tk() # Instatiate an instace of a window
window.title("YouTube Video Downloader")
window.geometry("700x500")
window.config(background= 'white') #'#0d1124'
window.resizable(False, False)

icon = PhotoImage(file = 'img.png')
window.iconphoto(True, icon)

url = StringVar()
path = StringVar()


# URL
url_label = Label(window, 
            text="URL:   ",
            font= ("Ariel", 10, 'bold'),
            relief= RAISED,
            bd= 10,
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
                 #relief=RAISED,
                 bd = 10,
                 padx= 5)
path_label.place(x = 5, y = 50)

path_entry = Entry(window,
                   font=("Ariel", 10, "normal"),
                   relief= RAISED,
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
downloadButton.pack()





window.mainloop()