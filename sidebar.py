import tkinter as tk
from tkinter import ttk


class Sidebar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.mainframe = ttk.Frame(parent, padding='3 3 12 12')
        self.mainframe.grid(column=0, row=1, rowspan=3)

        add_folder_button = ttk.Button(self.mainframe, text='add_folder')
        save_button = ttk.Button(self.mainframe, text='save')
        open_folder_button = ttk.Button(self.mainframe, text='open folder')

        buttons = [add_folder_button, save_button, open_folder_button]
        for i, b in enumerate(buttons):
            b.grid(column=1, row=i + 1)
