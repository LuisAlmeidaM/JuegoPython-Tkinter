import tkinter as tk

class Ventana:
    def __init__(self, ancho, alto):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Ventana principal")

        # Establecer el tamaño de la ventana
        self.ventana.geometry(f"{ancho}x{alto}")

        #Llamar al método para iniciar la ventana
        self.Iniciar()

    def Iniciar(self):
        self.ventana.mainloop() # Iniciar el bucle principal de la ventana

# Crear una instancia de la clase Ventana
if __name__ == "__main__":
    ventana = Ventana(640,480)