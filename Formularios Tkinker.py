import tkinter as tk
from tkinter import messagebox

def registar():
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    direccion = cdireccion.get()
    genero = obtener_seleccion()
    ciudades = obtener_ciudad()
    mensaje = f"Información registrada:\n\n"
    mensaje += f"Nombre: {nombre}\n"
    mensaje += f"Apellido: {apellido}\n"
    mensaje += f"Edad: {edad}\n"
    mensaje += f"Dirección: {direccion}\n"
    mensaje += f"Género: {genero}\n"
    mensaje += f"Ciudades seleccionadas: {', '.join(ciudades)}"
    messagebox.showinfo("Información Registrada", mensaje)

def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
        return "Masculino"
    elif seleccion == 2:
        print("Opción 2 seleccionada")
        return "Femenino"
    
def obtener_ciudad():
    seleccionados = cuadro_lista.curselection()
    ciudades = []
    for index in seleccionados:
        ciudades.append(cuadro_lista.get(index))
    return ciudades       
ventana = tk.Tk()
ventana.title("Tecnar APP")
ventana.geometry("800x600")
ventana.resizable(True, True)
nombre = tk.Label(ventana, text="Nombre: ")
nombre.place(x=9, y=10)
cnombre=tk.Entry(ventana, width=30)
cnombre.place(x=80, y=10)

apellido = tk.Label(ventana, text="Apellido: ")
apellido.place(x=9, y=40)
capellido= tk.Entry(ventana, width=30)
capellido.place(x=80, y=40)
edad = tk.Label(ventana, text="Edad: ")
edad.place(x=9, y=70)
cedad = tk.Entry(ventana, width=30)
cedad.place(x=80, y=70)
direccion = tk.Label(ventana, text="Dirección: ")
direccion.place(x=9, y=100)
cdireccion = tk.Entry(ventana, width=30)
cdireccion.place(x=80, y=100)
cuadro_lista = tk.Listbox(ventana, width=30, height=5, selectmode="multiple")
cuadro_lista.place(x=80, y=140)
elementos = ["Cartagena","Bucaramanga","Santa Marta","Bogotá","Medellín"]
for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

variable = tk.IntVar()
casilla_verificacion = tk.Radiobutton(ventana, text="Masculino", variable=variable,value=1  ,command=obtener_seleccion)
casilla_verificacion.place(x=80, y=250)
casilla_verificacion2 = tk.Radiobutton(ventana, text="Femenino", variable=variable, value=2 ,command=obtener_seleccion)
casilla_verificacion2.place(x=80, y=270)


botón = tk.Button(ventana, text="Registrar", command=registar)
botón.place(x=100, y=300)

ventana.mainloop()