import tkinter as tk
from tkinter import messagebox

def registrar():
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


tk.Label(ventana, text="Nombre: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
cnombre = tk.Entry(ventana, width=30)
cnombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Apellido: ").grid(row=1, column=0, padx=5, pady=5, sticky="e")
capellido = tk.Entry(ventana, width=30)
capellido.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad: ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
cedad = tk.Entry(ventana, width=30)
cedad.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Dirección: ").grid(row=3, column=0, padx=5, pady=5, sticky="e")
cdireccion = tk.Entry(ventana, width=30)
cdireccion.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Ciudades: ").grid(row=4, column=0, padx=5, pady=5, sticky="e")
cuadro_lista = tk.Listbox(ventana, width=30, height=5, selectmode="multiple")
cuadro_lista.grid(row=4, column=1, padx=5, pady=5)
elementos = ["Cartagena", "Bucaramanga", "Santa Marta", "Bogotá", "Medellín"]
for index, elemento in enumerate(elementos):
    cuadro_lista.insert(tk.END, elemento)


variable = tk.IntVar()
tk.Radiobutton(ventana, text="Masculino", variable=variable, value=1, command=obtener_seleccion).grid(row=5, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(ventana, text="Femenino", variable=variable, value=2, command=obtener_seleccion).grid(row=6, column=1, padx=5, pady=5, sticky="w")

tk.Button(ventana, text="Registrar", command=registrar).grid(row=7, column=1, padx=5, pady=5)

ventana.mainloop()
