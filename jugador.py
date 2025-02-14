import tkinter as tk

class Jugador:
    def __init__(self, canvas, rutaImagen, x, y):
        self.canvas = canvas
        self.rutaImagen = rutaImagen
        self.x = x
        self.y = y
        self.velocidad = 5
        self.movimiento = {'Up': False, 'Down': False, 'Left': False, 'Right': False}

        # Cargar imagen
        self.imagen = tk.PhotoImage(file=self.rutaImagen)

        # Dibujar Imagen en el canvas
        self.sprite = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.imagen)
    
    def Mover(self):
        # Mover al jugador según el estado de movimiento
        if self.movimiento['Up']:
            self.y -= self.velocidad
        if self.movimiento['Down']:
            self.y += self.velocidad
        if self.movimiento['Left']:
            self.x -= self.velocidad
        if self.movimiento['Right']:
            self.x += self.velocidad

        # Actualizar la posición en el canvas
        self.canvas.move(self.sprite, self.x - self.canvas.coords(self.sprite)[0], self.y - self.canvas.coords(self.sprite)[1])
    
    def Manejar_Tecla(self, event):
        # Cambiar el estado de movimiento según la tecla presionada
        if event.keysym in self.movimiento:
            self.movimiento[event.keysym] = True

    def Soltar_Tecla(self, event):
        # Cambiar el estado de movimiento cuando se suelta la tecla
        if event.keysym in self.movimiento:
            self.movimiento[event.keysym] = False