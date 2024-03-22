vacio = []
print('vacio:', vacio)
print('', len(vacio))

ropa = ['Camisa','pantalón','boxer','zapatos','reloj','franela']
print('ropa:', ropa)
print('numero de ropa:',len(ropa))
primera_ropa = ropa[0]
print(primera_ropa)
tercera_ropa = ropa[3]
print(tercera_ropa)
sexta_ropa = ropa[5]
print(sexta_ropa)

Datos_personales = ["Jesús David", "19", "1.85", "Soltero", "La central calle 21"]
print(Datos_personales)
Datos_personales.append("Sexo: Masculino")
Datos_personales.append("Parentesco: Padre")
print(Datos_personales)

it_companies = ["facebook","google", "microsoft", "apple","IBM","Oracle","Amazon"]
print(it_companies)
it_companies.insert(3, "twitter")
it_companies.insert(2, "Afinia")
print(it_companies)
verificar_compañias = "twitter" in it_companies
print("Es falso o verdadero que twitter es hace parte de las compañias")
print(verificar_compañias)
print("Es falso o verdadero que mango hace parte de las compañias")
verificar_compañias = "mango" in it_companies
print(verificar_compañias)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.pop(0)
print(it_companies)
del it_companies[1] 
print(it_companies)
it_companies.clear()
print(it_companies)