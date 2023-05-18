# CONDICIONALES.
# PRACTICANDO CON IF, ELIF Y ELSE:
valor = 0

if (valor < 0):
    print('El número es negativo')
elif (valor > 0):
    print('El número es positivo')
else:
    print('El número es igual a cero')

print("-----------------------------")

# CICLOS ITERATIVOS O LOOPS.
# PRACTICANDO CON FOR:
for n in range(1,10):
    print(n)

print("-----------------------------")

# PRACTICANDO CON WHILE:
num = 1
while (num < 10):
    print(num)
    num += 1

print("-----------------------------")

# PRACTICANDO CON BREAK:
for i in range(5):
    print(i)
    break

print("-----------------------------")

# BREAK CON FOR:
cadena = 'Python'

for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

print("-----------------------------")

# BREAK CON WHILE:
x = 5

while True:
    x -= 1
    print(x)
    if x == 0:
        break
print("Fin del bucle")

print("-----------------------------")

# CONTINUE CON FOR:
cadena = 'Python'

for letra in cadena:
    if letra == 'P':
        continue
    print(letra)