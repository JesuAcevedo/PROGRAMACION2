vuelo = {
    "Aereolinea":"Avianca",
    "Vuelo":"AV3102",
    "Origen":"CTG",
    "Destino":"MDE",
    "tipo_maleta":["Cabina","Mano","Bodega"]
}
print("tipo de maleta")
for maleta in vuelo["tipo_maleta"]:
    print(maleta)
print("\nDiccionario")
for key, value in vuelo.items():
    print(f"{key}:{value}")