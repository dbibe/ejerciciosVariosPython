#Ejercicio: Las Elecciones
# El programa primero recibe un número  N , la cantidad de votos totales que se realizaron. Luego recibe  N  votos en formato string, cada uno consiste en el nombre del candidato seleccionado. El programa debe calcular el ganador e imprimir su nombre, para este ejemplo se asume que no hay empates. Los nombres y la cantidad de candidatos es desconocida.

cantidadVotos = int(input(""))
candidatos = {}

for voto in range(cantidadVotos):
    candidato = input("")

    if candidato in candidatos:
        candidatos[candidato] += 1
    else:
        candidatos[candidato] = 1


candidatoElegido = ""
votos = 0 

for candidato, voto in candidatos.items():    
    if(voto > votos):
        candidatoElegido = candidato
        votos = voto

print(candidatoElegido)

