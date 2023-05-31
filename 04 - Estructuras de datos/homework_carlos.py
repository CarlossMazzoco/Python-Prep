# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
mi_lista = ["Tokyo","Ciudad de México","Wall Street","Londres","Paris","Nueva York"]
print(mi_lista)

print("-----------------------------")

# 2) Imprimir por pantalla el segundo elemento de la lista
print(mi_lista[1])

print("-----------------------------")

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(mi_lista[1:4])

print("-----------------------------")

# 4) Visualizar el tipo de dato de la lista
print(type(mi_lista[1:4]))

print("-----------------------------")

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(mi_lista[2:])

print("-----------------------------")
# 6) Visualizar los primeros 4 elementos de la lista
print(mi_lista[:4])

print("-----------------------------")

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
mi_lista.append("Tokyo")
mi_lista.append("Boston")
print(mi_lista)

print("-----------------------------")

# 8) Agregar otra ciudad, pero en la cuarta posición
mi_lista.insert(3, "Toronto")
print(mi_lista)

print("-----------------------------")

# 9) Concatenar otra lista a la ya creada
mi_lista.extend(["Barcelona","Dubai","Singapur"])
print(mi_lista)

print("-----------------------------")

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(mi_lista.index("Tokyo"))

print("-----------------------------")

# 11) ¿Qué pasa si se busca un elemento que no existe?

# print(mi_lista.index("Bruselas"))
# Arroja un error que indica que el elemento buscado no se encuentra en la lista.

# 12) Eliminar un elemento de la lista
mi_lista.remove("Tokyo")
print(mi_lista)

print("-----------------------------")

# 13) ¿Qué pasa si el elemento a eliminar no existe?

# print(mi_lista.remove("Bruselas"))
# Arroja un error que indica que el elemento buscado no se encuentra en la lista.

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo.
ultimo_elemento = mi_lista.pop()
print(ultimo_elemento)

# 15) Mostrar la lista multiplicada por 4
print(mi_lista * 4)

print("-----------------------------")

# 16) Crear una tupla que contenga los números enteros del 1 al 20
mi_tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(mi_tupla)

print("-----------------------------")

# 17) Imprimir desde el índice 10 al 15 de la tupla
print(mi_tupla[10:16])

print("-----------------------------")

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in mi_tupla)
print(30 in mi_tupla)

print("-----------------------------")


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print('Paris' in mi_lista)
print(f'El elemento "Paris" existe dentro de la lista creada.\n{mi_lista}, por lo cual no se agrega. ')

print("-----------------------------")

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
elemento_en_lista = mi_lista.count('Tokyo')
elemento_en_tupla = mi_tupla.count(13)

print(f'Tokyo se encuentra {elemento_en_lista} veces dentro de la lista.')
print(f'13 se encuentra {elemento_en_tupla} veces dentro de la tupla.')


print("-----------------------------")

# 21) Convertir la tupla en una lista
mi_lista2 = list(mi_tupla)
print(mi_lista2)

print("-----------------------------")

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
numero1, numero2, numero3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_ = mi_tupla

print(numero1)
print(numero2)
print(numero3)

print("-----------------------------")

# 23) Crear un diccionario utilizando la lista creada en el punto 1, asignándole la clave "ciudad". Agregar también otras claves, como puede ser "País" y "Continente".
lista_pais = ['México','USA','Canadá','Inglaterra','Francia','USA','Japón','USA','España','Emiratos Árabes']
lista_continente = ['America','America','America','Europa','Europa','America','Asia','America','Europa','Asia']


mi_diccionario = {
    'Ciudad':mi_lista,
    'País':lista_pais,
    'Continente':lista_continente
}

print(mi_diccionario)

print("-----------------------------")

# 24) Imprimir las claves del diccionario
print(mi_diccionario.keys())

print("-----------------------------")

# 25) Imprimir las ciudades a través de su clave
print(mi_diccionario["Ciudad"])