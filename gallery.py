import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Gallery(ttk.Frame):
    photo_area_length = 700

    def __init__(self, parent) -> None:
        super().__init__(parent)

        mainframe = ttk.Frame(parent, padding='3 3 12 12')
        mainframe.grid(column=1, row=2)

        # canvas for the photos
        photos_canvas = tk.Canvas(mainframe,
                                  height=self.photo_area_length,
                                  width=self.photo_area_length,
                                  borderwidth=0)
        photos_canvas.grid(column=2,
                           row=1,
                           rowspan=3,
                           sticky=(tk.N, tk.E, tk.S, tk.W))

        # TODO: maybe put this into a function?
        # open a photo
        path = './images/bmth.jpg'
        load = Image.open(path)
        # resize the photo to fit in the canvas
        new_size = self.resize_image(load.width, load.height)
        load = load.resize(new_size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        # img = ttk.Label(photos_frame, image=render)
        photos_canvas.image = render
        photos_canvas.create_image(self.photo_area_length / 2,
                                   self.photo_area_length / 2,
                                   image=photos_canvas.image,
                                   anchor='center')

        # buttons
        prev_button = ttk.Button(mainframe, text='<<')
        prev_button.grid(column=1, row=2, sticky=tk.E)

        next_button = ttk.Button(mainframe, text='>>')
        next_button.grid(column=3, row=2, sticky=tk.W)

    def resize_image(self, width, height):
        ratio = self.photo_area_length / max(width, height)
        new_sizes = (ratio * width, ratio * height)

        return tuple(map(int, new_sizes))
