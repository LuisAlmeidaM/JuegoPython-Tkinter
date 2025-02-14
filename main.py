import tkinter as tk
from jugador import Jugador

class Ventana:
    def __init__(self, ancho, alto):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Ventana principal")

        # Establecer el tamaño de la ventana
        self.ventana.geometry(f"{ancho}x{alto}")

        # Centrar la ventana
        self.CentrarVentana(ancho, alto)

        # Crear el Canvas
        self.CrearCanvas(ancho, alto)

        # Crear el jugador
        self.jugador = Jugador(self.canvas, "imagenes/jugador.png", 100,100)

        # Vincular las teclas del teclado a la función manejar_tecla del jugador
        self.ventana.bind("<KeyPress>", self.jugador.Manejar_Tecla)
        self.ventana.bind("<KeyRelease>", self.jugador.Soltar_Tecla)  # Para manejar la tecla soltada

        # Llamar al método de actualización
        self.Actualizar()

        #Llamar al método para iniciar la ventana
        self.Iniciar()

    def CentrarVentana(self, ancho, alto):
        # Obtener las dimesiones de la ventana
        anchoPantalla = self.ventana.winfo_screenwidth()
        altoPantalla = self.ventana.winfo_screenheight()

        #Calcular la posición x Y y de la ventana
        x = (anchoPantalla // 2) - (ancho // 2)
        y = (altoPantalla // 2) - (alto // 2)

        # Establecer la posición de la pantalla
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def CrearCanvas(self,ancho, alto):
        # Crear un Canvas con fondo verde
        self.canvas = tk.Canvas(self.ventana, width=ancho, height=alto, bg="green")
        self.canvas.pack()  # Agregar el Canvas a la ventana
    
    def Actualizar(self):
        # Mover al jugador
        self.jugador.Mover()
        # Programar la próxima actualización
        self.ventana.after(16, self.Actualizar) # Aproximadamente 60 FPS
    
    def Iniciar(self):
        self.ventana.mainloop() # Iniciar el bucle principal de la ventana

# Crear una instancia de la clase Ventana
if __name__ == "__main__":
    ventana = Ventana(640,480)
