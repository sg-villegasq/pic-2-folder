import tkinter as tk
from tkinter import ttk
import math


class Folders(ttk.Frame):
    n_buttons = 0

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.mainframe = ttk.Frame(parent, padding='3 3 12 12')
        self.mainframe.grid(column=1, row=3)

        # testing add_folders
        test_folders = []
        for i in range(5):
            test_folders.append(f'folder{i}')

        self.add_folders(test_folders)

    def add_folders(self, folder_list=[]):
        for folder in folder_list:
            self.add_new_button(folder)

    def add_new_button(self, text):
        self.n_buttons += 1

        row = math.ceil(self.n_buttons / 2)
        column = 1 if self.n_buttons % 2 else 2

        # keep this somewhere in the clas
        folder_button = ttk.Button(self.mainframe, text=text)
        folder_button.grid(column=column, row=row)
