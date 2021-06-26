import tkinter as tk
from tkinter import mainloop, ttk

from gallery import Gallery


class Pic2Folder(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Pic 2 Folder')

        mainframe = ttk.Frame(self, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.S, tk.E))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        title = ttk.Label(mainframe, text='<folder title>')
        title.grid(column=1, row=1)

        # add gallery
        Gallery(mainframe)

        # add folder/options section

        # add sidebar
