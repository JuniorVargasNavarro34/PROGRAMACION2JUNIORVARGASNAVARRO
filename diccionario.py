perro={}

perro ['nombre'] = "camilo"
perro ['color'] = "negro"
perro ['patas'] = "4"
perro ['raza'] = "pitbul"
perro ['edad'] = "3"

print(perro)

estudiante = {
    'nombre':'junior',
    'Apellido':'vargas',
    'años':40,
    'sexo':'masculino',
    'estado_civil':'Casado',
    'habilidades':'programador',
    'pais':'Colombia',
    'dirrecion':'Barrio Libano Calle 34b',
    }
print(estudiante)
print (len(estudiante))

alumno={}
print(len(alumno))

habilidades = ['Binero']
print(habilidades)
print(type(habilidades,))

habilidades = {
    'programacion': 'avanzado',
    'ingles': 'intermedio',
    'comunicacion': 'avanzado'
}

habilidades['trabajo en equipo'] = 'intermedio'
habilidades['liderazgo'] = 'avanzado'

print(habilidades)

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
claves = list(mi_diccionario.keys())
print(claves)

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
valores= list(mi_diccionario.values())
print(valores)

diccionario = {'a': 1, 'b': 2, 'c': 3}

lista_tuplas = list(diccionario.items())

print(lista_tuplas)
diccionario = {'a': 1, 'b': 2, 'c': 3}

if 'b' in diccionario:
    del diccionario['b']
    print("Elemento 'b' eliminado del diccionario")
else:
    print("La llave 'b' no está presente en el diccionario")
print(diccionario)
diccionario = {'a': 1, 'b': 2, 'c': 3}

del diccionario

print(diccionario)



