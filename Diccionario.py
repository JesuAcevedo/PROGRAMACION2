
perro = {}
perro ['nombre'] = 'Toby'
perro['Color'] = 'Negro'
perro['Raza'] = 'Doberman'
perro['Patas'] = '4'
perro['edad'] ='6 años'
print(perro)
Estudiante = {}
Estudiante ['nombre'] = 'Jesús'
Estudiante['Apellido'] = 'Acevedo'
Estudiante['Sexo'] = 'Masculino'
Estudiante['Edad']= '19'
Estudiante ['Estado civil'] = 'Soltero'
Estudiante ['habilidades']= 'Soy bueno nadando'
Estudiante ['país'] = 'Colombia'
Estudiante ['Ciudad'] = 'Cartagena'
Estudiante ['Dirección'] = 'Blas de lezo calle 21'
Estudiante['habilidades'] = 'Retengo buena información y tengo bastante paciencia'
print(len(Estudiante))
print(Estudiante['habilidades'])
print('habilidades' in Estudiante)
keys = Estudiante.keys()
print(keys)
values = Estudiante.values()
print(values)
print(Estudiante.items())
Estudiante.pop('nombre')

print(Estudiante)
del Estudiante


