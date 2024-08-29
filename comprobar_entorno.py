import tkinter as tk
import pygame
from OpenGL.GL import glGetString, GL_VERSION
import ctypes

def obtener_version_opengl():
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.OPENGL | pygame.DOUBLEBUF)
    version = glGetString(GL_VERSION)
    pygame.quit()
    return ctypes.c_char_p(version).value.decode("utf-8")

def mostrar_version():
    version = obtener_version_opengl()
    label_version.config(text=f"Versión de OpenGL: {version}")

# Crear la ventana principal de tkinter
ventana = tk.Tk()
ventana.title("Información de OpenGL")

# Crear y posicionar los widgets
label_titulo = tk.Label(ventana, text="Versión de OpenGL instalada:", font=("Arial", 14))
label_titulo.pack(pady=10)

label_version = tk.Label(ventana, text="", font=("Arial", 12))
label_version.pack(pady=10)

boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.quit, font=("Arial", 12))
boton_cerrar.pack(pady=20)

# Obtener y mostrar la versión de OpenGL
mostrar_version()

# Ejecutar la interfaz gráfica
ventana.mainloop()
