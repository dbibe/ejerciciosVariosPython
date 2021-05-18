#Ejercicio: El Ahorcado
# Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y otro jugador intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree que se encuentra en la palabra elegida.
# Una vez que el segundo jugador adivina todas las letras que se encuentran en la palabra, el juego termina y se muestra la cantidad de intentos que fueron necesarios. En el caso de que la cantidad de intentos errados supere cierto límite, el juego termina y el segundo jugador pierde. En esta versión del juego, si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias cuentan como adivinadas.

# Formato del input:
# Primero se recibe la palabra que se debe adivinar (en mayúsculas).
# Luego se recibe un número  N , la cantidad máxima de intentos errados.
# Por último se recibe cierta cantidad de letras en mayúsculas, una por línea, sin repetir.

# Formato del output:
# En caso de que se haya adivinado la palabra antes de superar el límite  N , se imprime la cantidad de intentos que tardó en adivinar.
# En caso de que se haya superado el límite  N , se imprime el número  0 .

palabraadivinar = input("Ingrese palabra: ")
cantMaxErrores = int(input("Ingrese cantidad maxima de intentos "))

if cantMaxErrores >= 100:
    exit(-1)

letra=input("")

contador = 0
cantAdivinadas = 0

while len(palabraadivinar)!= 0 and (contador<=cantMaxErrores):
    if letra in palabraadivinar:
        palabraadivinar = palabraadivinar.replace(letra,"")
        cantAdivinadas += 1
        if len(palabraadivinar)!= 0:
            letra = input("")
    else:
        contador +=1
        letra = input("")


if(contador <= cantMaxErrores):
    valorTotal = cantAdivinadas + contador
    print(valorTotal)
else:
    print(0)