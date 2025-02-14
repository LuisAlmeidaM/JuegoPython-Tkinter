import tkinter as tk

class Jugador:
    def __init__(self, canvas, rutaImagen, x, y):
        self.canvas = canvas
        self.rutaImagen = rutaImagen
        self.x = x
        self.y = y

        # Cargar imagen
        self.imagen = tk.PhotoImage(file=self.rutaImagen)

        # Dibujar Imagen en el canvas
        self.sprite = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.imagen)