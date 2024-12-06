import random
import json
import os
import time

'''
def generar_matriz(filas, columnas): #cambiar nombre a tablero

    matriz = []  
    for i in range(filas):
        piezas = []
        for a in range(columnas):
            numero = random.randint(1, 3) 
            piezas.append(numero)
        matriz.append({"piezas": piezas})
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila["piezas"])


lista = [
{"piezas":[]},
{"piezas":[]},
{"piezas":[]},
{"piezas":[]}
]





def solicitar_posicion():
    while True:
        fila = int(input("Fila: Ingrese un numero del [0-3]: "))
        columna = int(input("Columna: Ingrese un numero del [0-6]: "))

        if 0 <= fila <= 3 and 0 <= columna <= 6:
                    return fila, columna
        else:
                print("Error. Por favor ingrese una fila entre 0 y 3, y una columna del 0 al 6.")
        


def verificar_tres_juntos(matriz, fila, columna):
    numero_elegido = matriz[fila]["piezas"][columna] #marco como numero elegido la posicion que elige el usuario
    contador_abajo = 0
    contador_arriba = 0
    
    for i in range(fila, len(matriz)):#abajo
        if matriz[i]["piezas"][columna] == numero_elegido:
            contador_abajo += 1 #aumento contador si coincide numero, sino, corta
        else:
            break 

    for i in range(fila, -1,-1):#vuelvo hacia arriba si encuentro num aumento
        if matriz[i]["piezas"][columna] == numero_elegido:
              contador_arriba += 1
        else:
             break
#armar una funcion para modularizar


for i in range(-1, 2):  # arriba, inicial, abajo
        a = fila + i
        
        if a >= 0 and a < len(matriz):
            if matriz[a]["piezas"][columna] == numero_elegido:
                if i == -1:  #arriba
                    contador_arriba += 1
                elif i == 1:  # abajo
                    contador_abajo += 1
  
    return contador_abajo, contador_arriba


    if contador_abajo + (contador_arriba -1) >= 3:
        
        print("Ha ganado 10 puntos")
    else:
        print("Segui participando")
        



def correr_juego():
    print("¡Bienvenido al canddyyy=?")
    
    nombre = input("Ingresa tu nombre: ")

    filas = 7
    columnas = 7
    tablero = generar_tablero(filas, columnas)
    
    tiempo_restante = 10
    puntaje = 0

    while tiempo_restante > 0:
        print(f"Tiempo restante: {tiempo_restante} segundos")
        imprimir_tablero(tablero)

        fila, columna = solicitar_posicion()
    
#iniciar tiempo, para poder checkear y generar los puntos y demas

        if verificar_columna(tablero, columna):
            print("Ganaste 10 puntos titán del pacífico.")
            puntaje += 10
        else:
            print("Ponele voluntad.....")
            tablero = generar_tablero(filas, columnas)
            tiempo_restante -= 1
            puntaje -= 1

        tiempo_restante -= 1  vamos restando el tiempo
         
     print(f"El juego ha terminado. Tu puntaje final es: {puntaje} puntos")
    guardar_puntaje_json(nombre, puntaje)

#creacion archivo, verificar/acomodar: acordarse d eimportar el json, IMPORTANTE


def guardar_puntaje_json(nombre, puntaje):
    if os.path.exists("score.json"):
        # Si el archivo existe, leer los puntajes actuales
        with open("score.json", mode="r") as file:
            scores = json.load(file)
    else:
        scores = []

    scores.append({"nombre": nombre, "puntaje": puntaje})

    with open("score.json", mode="w") as file:
        json.dump(scores, file, indent)

        
def menu():
    while True:
        print("\nMenú de Juego:")
        print("1. Jugar")
        print("2. Ver Puntajes")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_puntajes()
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        

#final= no defini variables, terminar


print(f"El juego ha terminado. Tu puntaje final es: {puntaje} puntos")

guardar_puntaje(nombre, puntaje)
guardar_puntaje_json(nombre, puntaje)

'''