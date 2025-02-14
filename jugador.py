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
    
    def Mover(self, dx, dy):
        # Mover al jugador
        self.x += dx
        self.y += dy

        self.canvas.move(self.sprite, dx, dy)
    
    def Manejar_Tecla(self, event):
        # Mover el jugador según la tecla presionada
        if event.keysym == "Up":
            self.Mover(0, -5)  # Mover hacia arriba
        elif event.keysym == "Down":
            self.Mover(0, 5)   # Mover hacia abajo
        elif event.keysym == "Left":
            self.Mover(-5, 0)  # Mover hacia la izquierda
        elif event.keysym == "Right":
            self.Mover(5, 0)   # Mover hacia la derecha