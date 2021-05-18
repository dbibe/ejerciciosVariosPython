#Ejercicio: Conjetura Dr Lothar
# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

# Si el numero es par, se debe dividir por  .
# Si el numero es impar, se debe multiplicar por  y sumar .
# Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

# El input se recibe utilizando el comando input() sin ningún mensaje dentro de los paréntesis. El output se muestra usando print() y mostrándo ÚNICAMENTE el resultado, sin ningún texto adicional.

numero = int(input())

def lothar(numero):
    cantidad = 0
    while numero>1:
        if (numero%2 == 0):
            numero = numero/2
        else:
            numero = 3*numero + 1
        cantidad +=1
    return cantidad

print(lothar(numero))


