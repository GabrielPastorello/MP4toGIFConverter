from moviepy.editor import *
from tkinter import *
from tkinter import filedialog
from ttkthemes import themed_tk as tk
from PIL import Image
from tkinter import messagebox
import os

def add_video():
    video = filedialog.askopenfilename(title='Select Video', filetype=(('MP4 files', '*.mp4'),))
    file_box.insert(END, video)

def delete():
    for item in reversed(file_box.curselection()):
        file_box.delete(item)


def convert():
    file_box.select_set(0, END)
    address = []
    seconds = clicked.get()
    for item in file_box.curselection():
        address.append(str(file_box.get(item)))
    address_ = address[0]
    clip = VideoFileClip(address_) 
    filename = os.path.basename(address_)
    filename = filename[:-3]+'gif'
    clip = clip.subclip(0, seconds) # Número de segundos
    clip.write_gif(filename)
    messagebox.showinfo("GIF Successfully Converted", "Your GIF was successfully created.\nCheck the folder where this program is located.")

screen = tk.ThemedTk()
screen.get_themes()
screen.set_theme("breeze")

width_of_window = 600
height_of_window = 520
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x_coordinate = int((screen_width/2) - (width_of_window/2))
y_coordinate = int((screen_height/2) - (height_of_window/2))
screen.geometry("{}x{}+{}+{}".format(width_of_window, height_of_window, x_coordinate, y_coordinate))

screen.title('MP4 to GIF Converter')
screen.iconbitmap('gif.ico')
screen.config(background='#136b75')

list_frame = Frame(screen)
list_frame.config(background='#136b75')
my_scrollbar = Scrollbar(list_frame, orient=VERTICAL)
file_box = Listbox(list_frame, width=400, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=file_box.yview)
my_scrollbar.pack(side=RIGHT, fill=Y, pady=15)
list_frame.pack(padx=30)
file_box.pack(pady=15)

button_select = Button(screen, text='Select File', command=add_video, background='white', fg='black', font=('Helvetica', 16), borderwidth=5)
button_select.pack(pady=15)

button_delete = Button(screen, text='Delete File', command=delete, background='white', fg='black', font=('Helvetica', 12))
button_delete.pack(pady=15)

time = [1, 2, 3, 4, 5, 6, 7, 8]

clicked = StringVar()
clicked.set(time[2])

button_frame = LabelFrame(screen, text="How many seconds since the video start?", font=('Helvetica', 10, 'bold'), background='#136b75', fg='white', labelanchor='n')
button_frame.pack(pady=10)
drop = OptionMenu(button_frame, clicked, *time)
drop.pack(pady=10)
drop.config(highlightbackground='#136b75', fg='black')

button_convert = Button(screen, text='CONVERT', command=convert, background='black', fg='white', font=('Helvetica', 18, 'bold'), borderwidth=6)
button_convert.pack(pady=15)

screen.mainloop()
