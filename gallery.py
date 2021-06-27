import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os


class Gallery(ttk.Frame):
    photo_area_length = 700
    valid_filetypes = [
        '.jpg', '.jpeg', '.gif', '.tiff', '.bmp', '.ppm', '.png'
    ]

    def __init__(self, parent) -> None:
        super().__init__(parent)

        mainframe = ttk.Frame(parent, padding='3 3 12 12')
        mainframe.grid(column=1, row=2)

        # canvas for the photos
        self.photos_canvas = tk.Canvas(mainframe,
                                       height=self.photo_area_length,
                                       width=self.photo_area_length,
                                       borderwidth=0)
        self.photos_canvas.grid(column=2,
                                row=1,
                                rowspan=3,
                                sticky=(tk.N, tk.E, tk.S, tk.W))

        path = filedialog.askdirectory()
        self.imgs = self.list_images(path)
        # open the first photo
        self.current = 0
        self.open_image(self.imgs[self.current])

        # buttons
        prev_button = ttk.Button(mainframe,
                                 text='<<',
                                 command=lambda: self.move(-1))
        prev_button.grid(column=1, row=2, sticky=tk.E)

        next_button = ttk.Button(mainframe,
                                 text='>>',
                                 command=lambda: self.move(+1))
        next_button.grid(column=3, row=2, sticky=tk.W)

    def list_images(self, path):
        file_list = os.listdir(path)
        images = [
            os.path.join(path, f) for f in file_list
            if os.path.splitext(f)[-1].lower() in self.valid_filetypes
        ]

        return images

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

    def move(self, delta):
        self.current += delta
        # start again when we reach the end
        position = self.current % len(self.imgs)
        self.open_image(self.imgs[position])
