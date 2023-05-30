mi_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde']

print(mi_lista)
print(type(mi_lista))
print(mi_lista[2])
print(mi_lista[0:2])
print(mi_lista[:2])
print(mi_lista[0:])

print("-----------------------------")

# Agregando un elemento al final de la lista(Si el elemento ya existe va a quedar duplicado)
mi_lista.append('Blanco')
print(mi_lista)

print("-----------------------------")

# Agrando un elemento duplicado al final.
mi_lista.append('Blanco')
print(mi_lista)

print("-----------------------------")

# Agregando un elemento especifico por el índice(el elemento existente en dicho indice, se desplaza hacia adelante)
mi_lista.insert(3, 'Negro')
print(mi_lista)

print("-----------------------------")

# Concatenar una nueva lista a la lista previamente creada.
mi_lista.extend(['Marron', 'Gris'])
print(mi_lista)

print("-----------------------------")

#Encontrando el índice de un valor en específico.
print(mi_lista.index('Azul'))

print("-----------------------------")

# Eliminando un elemento de la lista.
mi_lista.remove('Blanco')
print(mi_lista)
mi_lista.remove('Blanco')
print(mi_lista)
mi_lista.remove('Negro')
print(mi_lista)

print("-----------------------------")

# Extraer y recuperar el último elemento de la lista.
ultimo = mi_lista.pop()
print(ultimo)
print(mi_lista)

print("-----------------------------")

# Multiplicando la lista 3 veces.
print(['a','b','c'] * 3)

print("-----------------------------")

# Ordenando una lista de menor a mayor.
lista = [1,4,3,6,8,2]
lista.sort()
print(lista)

print("-----------------------------")

# Ordenando una lista de mayor a menor.
lista = [1,4,3,6,8,2]
lista.sort(reverse=True)
print(lista)

print("-----------------------------")

# Convirtiendo una lista en tupla.
mi_tupla = tuple(mi_lista)
print(mi_tupla[1])

print("-----------------------------")

# Evaluar si un elemento está contenido en la tupla.
print('Rojo' in mi_tupla)

print("-----------------------------")

# Evaluando las veces que está un elemento específico.
print(mi_tupla.count('Rojo'))

print("-----------------------------")

# Tupla con un solo elemento.
mi_tupla_unitaria = ('Blanco')
print(mi_tupla_unitaria)

print("-----------------------------")

# Empaquetado de tupla.
mi_tupla = 'Gaspar', 5, 8, 1999
print(mi_tupla)

print("-----------------------------")

# Desempaquetado de tupla, se guardan los valores en orden de las variables.
nombre, dia, mes, año = mi_tupla
print(f'Nombre: {nombre}.\nDia: {dia}\nMes: {mes}\nAño: {año}')

print("-----------------------------")

# convertir una tupla en lista.
mi_lista = list(mi_tupla)
print(mi_lista)

print("-----------------------------")

# Diccionarios.
mi_diccionario = {
    'Colores Primarios': ['Rojo','Azul','Amarillo'],
    'Colores Secundarios': ['Naranja','Violeta','Verde'],
    'Clave3': 10,
    'Clave4': False
}

print("-----------------------------")

# Imprimiendo un valor a través de su clave.
print(mi_diccionario['Colores Secundarios'])

print("-----------------------------")

# Agregar un valor.
mi_diccionario['Clave5'] = 'Otro ejemplo'
print(mi_diccionario['Clave5'])

print("-----------------------------")

# Cambiar un valor.
mi_diccionario['Clave3'] = 2
print(mi_diccionario['Clave3'])

print("-----------------------------")

# Eliminar un elemento de un diccionario a través de su clave.
del mi_diccionario['Clave4']
print(mi_diccionario)

print("-----------------------------")

# Utilizar una tupla como clave de un diccionario.
mi_tupla = ("Argentina", "Italia", "Inglaterra")
mi_diccionario = {
    mi_tupla[0]:"Buenos Aires",
    mi_tupla[1]:"Roma",
    mi_tupla[2]:"Londres"
}
print(mi_diccionario)

print("-----------------------------")

# Colocar una tupla dentro de un diccionario.
mi_diccionario = {
    'Clave1':'Valor1',
    'Clave2':(1,2,3,4,5)
}
print(mi_diccionario)

print("-----------------------------")

# Colocar una lista dentro de un diccionario.
mi_diccionario = {
    'Clave1':'Valor1',
    'Clave2':[1,2,3,4,5]
}
print(mi_diccionario)

print("-----------------------------")

# Colocar un diccionario dentro de un diccionario.
mi_diccionario = {
    'Clave1':'Valor1',
    'Clave2':{
        'números':[1,2,3,4,5]
        }
}
print(mi_diccionario)

print("-----------------------------")

# Imprimir las claves del diccionario.
print(mi_diccionario.keys())

print("-----------------------------")

# Imprimir los valores del diccionario.
print(mi_diccionario.values())

print("-----------------------------")

# Imprimir la longitud del diccionario.
print(len(mi_diccionario))

