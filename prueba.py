def imprimir_menu():
        print("menu")
        print("1.Personas")
        print("2.Vehiculos")
        print("3.universidades")
        print("4.notas")
        print("5.salir")
def seleccionar_opcion(opcion):
        if opcion == '1':
            print("Hola, has presionado la opción Personas")
        elif opcion == '2':
            print("Hola, has presionado la opción Vehículos")
        elif opcion == '3':
            print("Hola, has presionado la opción Universidades")
        elif opcion == '4':
            print("Hola, has presionado la opción Notas")
        elif opcion == '5':
            print("Chao, perdí el parcial de redes en 2.6")
        else:
         print("Opción inválida")
while True:
    imprimir_menu()
    opcion = input("Selecciona una opción: ")
    seleccionar_opcion(opcion)
    if opcion == '5':
            break         