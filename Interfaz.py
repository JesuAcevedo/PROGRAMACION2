import tkinter as tk 
from PIL import Image, ImageTk
def cambiar_texto():
    etiqueta.config(text="Texto cambiado")
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    if texto_ingresado:
        etiqueta.config(text="Texto ingresado: " + texto_ingresado)
    else:
        etiqueta.config(text="No se ha ingresado texto")
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")
        
def obtener_seleccion2():
    seleccion2 = variable2.get()
    if seleccion2 == 1:
        print("Opción 1 seleccionada")
    elif seleccion2 == 2:
        print("Opción 2 seleccionada")
    elif seleccion2 == 3:
        print("Opción 3 seleccionada")
def obtener_seleccion3():
    seleccion3 = variable3.get()
    if seleccion3 == 1:
        print("Opción 1 seleccionada")
    elif seleccion3 == 2:
        print("Opción 2 seleccionada")
    elif seleccion3 == 3:
        print("Opción 3 seleccionada")
        
ventana = tk.Tk()
path = Image.open("prueba2.jpg")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
ventana.title("Tecnar APP")
ventana.geometry("500x500")

ventana.resizable(True,True)
etiqueta = tk.Label(ventana, text="Escriba su nombre completo: ")
etiqueta.pack()
cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()
boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()



variable = tk.IntVar()
etiqueta2 = tk.Label(ventana, text="Estado civil: ")
etiqueta2.pack()


opcion1 = tk.Radiobutton(ventana, text="Situación complicada", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Soltero", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Casado", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()

etiqueta3 = tk.Label(ventana, text="Con cuantas personas vive: ")
etiqueta3.pack()
variable2 = tk.IntVar()
opcion4 = tk.Radiobutton(ventana, text="2", variable=variable2, value=1, command=obtener_seleccion2)
opcion4.pack()

opcion5 = tk.Radiobutton(ventana, text="3", variable=variable2, value=2, command=obtener_seleccion2)
opcion5.pack()

opcion6 = tk.Radiobutton(ventana, text="4", variable=variable2, value=3, command=obtener_seleccion2)
opcion6.pack()
variable3 = tk.IntVar()
etiqueta4 = tk.Label(ventana, text="Seleccione el número de creditos: ")
etiqueta4.pack()

opcion7 = tk.Radiobutton(ventana, text="16", variable=variable3, value=1, command=obtener_seleccion2)
opcion7.pack()

opcion8 = tk.Radiobutton(ventana, text="17", variable=variable3, value=2, command=obtener_seleccion2)
opcion8.pack()

opcion9 = tk.Radiobutton(ventana, text="19", variable=variable3, value=3, command=obtener_seleccion2)
opcion9.pack()


etiqueta5 = Image.open("thax.jpeg")
imagen_tk = ImageTk.PhotoImage(etiqueta5)
imagen_label = tk.Label(ventana, image=imagen_tk, anchor="center", width=300, height=300)
imagen_label.pack()
ventana.mainloop()



