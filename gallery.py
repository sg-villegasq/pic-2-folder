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
        self.photos_canvas = tk.Canvas(mainframe,
                                       height=self.photo_area_length,
                                       width=self.photo_area_length,
                                       borderwidth=0)
        #    bg='dim gray')
        self.photos_canvas.grid(column=2,
                                row=1,
                                rowspan=3,
                                sticky=(tk.N, tk.E, tk.S, tk.W))

        # open a photo
        path = './images/test.jpg'
        self.open_image(path)

        # buttons
        prev_button = ttk.Button(mainframe, text='<<')
        prev_button.grid(column=1, row=2, sticky=tk.E)

        next_button = ttk.Button(mainframe, text='>>')
        next_button.grid(column=3, row=2, sticky=tk.W)

    def open_image(self, path):
        canvas_position = self.photo_area_length // 2
        try:
            load = Image.open(path)
        except FileNotFoundError:
            self.photos_canvas.configure(bg='dim gray')
            self.photos_canvas.create_text(canvas_position,
                                           canvas_position,
                                           text='Photo not found!',
                                           anchor=tk.CENTER)
        else:
            # resize the image to fit the canvas
            new_dimensions = self.resize_image(load.width, load.height)
            load = load.resize(new_dimensions, Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            # place the image inside the canvas
            self.photos_canvas.image = render
            self.photos_canvas.create_image(canvas_position,
                                            canvas_position,
                                            image=self.photos_canvas.image,
                                            anchor=tk.CENTER)

    def resize_image(self, width, height):
        ratio = self.photo_area_length / max(width, height)
        new_sizes = (ratio * width, ratio * height)

        return tuple(map(int, new_sizes))
