import tkinter as tk
from tkinter import ttk


class Gallery(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        mainframe = ttk.Frame(parent, padding='3 3 12 12')
        mainframe.grid(column=1, row=1)

        # place for the photos
        photos_frame = ttk.Frame(mainframe,
                                 height=240,
                                 width=240,
                                 relief='groove')
        photos_frame.grid(column=2, row=1, rowspan=3)

        # buttons
        prev_button = ttk.Button(mainframe, text='<<')
        prev_button.grid(column=1, row=2, sticky=tk.E)

        next_button = ttk.Button(mainframe, text='>>')
        next_button.grid(column=3, row=2, sticky=tk.W)
