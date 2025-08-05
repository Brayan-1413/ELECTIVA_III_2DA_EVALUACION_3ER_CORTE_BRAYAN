from tkinter import *

def centrar_pantalla(root, ancho, altura):
 
        ancho_pantalla=root.winfo_screenwidth()
        altura_pantalla=root.winfo_screenheight()
        
        coordenas_x= int((ancho_pantalla/2)-(ancho/2))
        coordenas_y= int((altura_pantalla/2)-(altura/2))
        
        root.geometry(f'{ancho}x{altura}+{coordenas_x}+{coordenas_y}')