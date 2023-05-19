import math 
## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

a = 10
print(f'Mi número entero es: {a}')

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))

# 4) Crear una variable que contenga tu nombre
mi_nombre = "Carlos"

# 5) Crear una variable que contenga un número complejo
num_complejo = 4 + 8j


# 6) Mostrar el tipo de dato de la variable creada en el punto 5
print(type(num_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi_redondeado = round(math.pi,4)
print(pi_redondeado)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
true_string = 'True'
true_booleano = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(true_string))
print(type(true_booleano))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma_entero_decimal = 10 + 15.5
print(suma_entero_decimal)
# 11) Realizar una operación de suma de números complejos
num_complejo2 = 4 + 12j
num_complejo3 = 8 + 27j
print(num_complejo2 + num_complejo3)
# 12) Realizar una operación de suma de un número real y otro complejo
num_real = 12
num_complejo4 = 4 + 9j
resultado = num_real + num_complejo4
print(resultado)
# 13) Realizar una operación de multiplicación
mult = 23 * 2
print(mult)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
pot = 2**8
print(pot)
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
div = 27 / 4
print(div)

# 16) De la división anterior solamente mostrar la parte entera
div_ent = 27 // 4
print(div_ent)

# 17) De la división de 27 entre 4 mostrar solamente el resto
div_rest = 27 % 4
print(div_rest)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
mi_num = 4
resultado2 = (div_ent * mi_num) + div_rest
print(resultado2)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
saludo = "Buenos días "
persona = "Carlos"
print(saludo + persona)
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print(2 == "2")
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int("2"))
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
var_con_coma = "3,8"
var_convertida = var_con_coma.replace(',','.')
var_con_punto = float(var_convertida)
print(f'Arroja error porque {var_con_punto} estaba representado con , y no con . ')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var = 3
var -= 1
print(var)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
op = 1 << 2
print(op)
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# print(2 + '2')
problem = "2 + '2'"
print(f"No está permitida la operación {problem} porque son tipos de datos distintos, no es posible sumar un str a un int/float/boolean")

# 26) Realizar una operación válida entre valores de tipo entero y string
var_ent = 5
var_str = "Jajajaja"

print(f'Cuando algo nos da risa lo plasmamos en texto de la siguiente manera: {var_ent * var_str}')