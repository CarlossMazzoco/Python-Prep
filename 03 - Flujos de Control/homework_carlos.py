## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var = 18
if var < 0:
    print(f"{var} Es menor que 0")
elif var > 0:
    print(f"{var} Es mayor que 0")
else:
    print(f"{var} Es igual a 0")

print("-----------------------------")
# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
var2 = 48
var3 = "Jaja"

if type(var2) == type(var3):
    print(f"{var2} y {var3} son del mismo tipo de dato.")
else:
    print(f"{var2} es: {type(var2)} y {var3} es: {type(var3)}, por lo tanto no son del mismo tipo de dato.")

print("-----------------------------")
# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range (1,21):
    if (n % 2 == 0):
        print(f'El numero {n} es par')
    else:
        print(f'El numero {n} es impar')


print("-----------------------------")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    resultado = i**3
    print(f" El valor de {i} elevado a la 3era potencia es: {resultado}")

print("-----------------------------")

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

num_entero = 10
for numero in range(num_entero):
    print(numero)

print("-----------------------------")

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
numero2 = 5
factorial_numero = 1

while numero2 > 1:
    factorial_numero *= numero2
    numero2 -= 1

print(f"El factorial de 5 es: {factorial_numero}")

print("-----------------------------")

# 7) Crear un ciclo for dentro de un ciclo while
numero3 = 5
while numero3 > 0:
    for i in range(numero3):
        print(numero3)
        numero3 -=1

print("-----------------------------")


# 8) Crear un ciclo while dentro de un ciclo for
numero4 = 10
for i in range(numero4):
    while numero4 < 10:
        print(i)

print("-----------------------------")

# 9) Imprimir los números primos existentes entre 0 y 30 
for num in range(2, 31):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)

print("-----------------------------")

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
for num in range(2, 31):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            continue
    if es_primo:
        print(num)

print("-----------------------------")


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

### EL EJERCICIO LO HICE ANTES DE VER EL VIDEO DE CLASE, EN ESTE CASO LO UNICO QUE HICE FUE CAMBIAR EL USO DE "CONTINUE" Y "BREAK", PERO EN ESTE CASO NO SE LLEVO A CABO NINGUNA OPTIMIZACION. 

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

### EN EL CASO DE MI DESARROLLO DE LOS EJERCICIOS NO PODRIA EXISTIR UN CAMBIO RELACIONADO AL INCREMENTO DE NUMEROS Y LA OPTIMIZACION.

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(f'{n} es divisible por 12')

print("-----------------------------")

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usuario de buscar el siguiente

while True:
    entrada = input("Ingresa un número (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        break

    try:
        numero = int(entrada)
        if numero < 2:
            print("Por favor, ingresa un número mayor o igual a 2.")
            continue

        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            print("El número {} es primo.".format(numero))
        else:
            siguiente_primo = numero + 1
            while True:
                es_primo = True
                for i in range(2, int(siguiente_primo ** 0.5) + 1):
                    if siguiente_primo % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    break
                siguiente_primo += 1

            print("El número {} no es primo.".format(numero))
            print("El siguiente número primo es {}.".format(siguiente_primo))
    except ValueError:
        print("Por favor, ingresa un número válido.")


print("-----------------------------")

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1

print("-----------------------------")