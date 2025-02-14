import tkinter as tk

class Ventana:
    def __init__(self, ancho, alto):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Ventana principal")

        # Establecer el tamaño de la ventana
        self.ventana.geometry(f"{ancho}x{alto}")

        # Centrar la ventana
        self.CentrarVentana(ancho, alto)

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

    def Iniciar(self):
        self.ventana.mainloop() # Iniciar el bucle principal de la ventana

# Crear una instancia de la clase Ventana
if __name__ == "__main__":
    ventana = Ventana(640,480)