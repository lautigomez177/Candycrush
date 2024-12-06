import random
import json
import time
import os
import pygame
import config
from config import CELDAS, ANCHO, ALTO,FONDO, FILAS, COLUMNAS, NEGRO, BLANCO, ROJO, FUENTE, INPUTBOX, BOTONRECT


pygame.init()

def generar_matriz(filas, columnas):

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


def solicitar_posicion():
    while True:
        fila = int(input("Fila: Ingrese un numero del [0-3]: "))
        columna = int(input("Columna: Ingrese un numero del [0-6]: "))  #pido

        if 0 <= fila <= 3 and 0 <= columna <= 6:    #valido
                    return fila, columna
        else:
                print("Error. Por favor siga las indicaciones del ingreso de datos.")

def verificar_tres_juntos(matriz, fila, columna):
    pieza = matriz[fila]["piezas"][columna]  # pieza clickeada/solicitada

 
    piezas_en_vertical = 1  # pieza actual

    
    for i in range(1, 3):  # verif arriba hasta 2 piezas
        if fila - i >= 0 and matriz[fila - i]["piezas"][columna] == pieza:
            piezas_en_vertical += 1
        else:
            break  # si es diferente, rompe


    for i in range(1, 3):  # verif hasta 2 abajo
        if fila + i < len(matriz) and matriz[fila + i]["piezas"][columna] == pieza:
            piezas_en_vertical += 1
        else:
            break  # si es dif rompe

    if piezas_en_vertical >= 3:    # si hay 3 o mas iguales, true
        return True

    return False      #sino fals

def guardar_puntaje_json(nombre_jugador, puntaje):
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as file:
            scores = json.load(file)
    else:
        scores = []

    scores.append({"nombre": nombre_jugador, "puntaje": puntaje})

    with open("puntajes.json", "w") as file:
        json.dump(scores, file)






def mostrar_puntajes():
    if not os.path.exists("score.json"):
        print("No hay puntajes registrados aún")

    else: 
        with open("score.json", mode="r") as file:     #si no hay, no hay, sino, los leo
            score = json.load(file)

        print("Puntajes: ")
        for score in score:
            print(f"{score['nombre']}: {score['puntaje']} puntos")





def correr_juego():
    print("¡Bienvenido al canddyyy=?")
    
    nombre = input("Ingresa tu nombre: ")

    filas = 7
    columnas = 7
    tablero = generar_matriz(filas, columnas)
    
    tiempo_inicial = time.time()
    
    tiempo_restante = 10
    puntaje = 0

    while tiempo_restante > 0:
        
        tiempo_transcurrido = time.time() - tiempo_inicial
        
        tiempo_restante = 10 - int(tiempo_transcurrido)

        print(f"Tiempo restante: {tiempo_restante} segundos")
        imprimir_matriz(tablero)

        fila, columna = solicitar_posicion()
    

        if verificar_tres_juntos(tablero, fila, columna):
            print("Ganaste 10 puntos titán del pacífico.")
            puntaje += 10
        
        else:
            print("Ponele voluntad.....")
            tablero = generar_matriz(filas, columnas)
            tiempo_restante -= 1
            puntaje -= 1

        tiempo_restante -= 1  #vamos restando el tiempo

        if tiempo_restante <= 0:
            break

    print(f"El juego ha terminado. Tu puntaje final es: {puntaje} puntos")
    guardar_puntaje_json(nombre, puntaje)



def menu():
    while True:
        print("\nMenú de Juego:")
        print("1. Jugar")
        print("2. Ver Puntajes")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            correr_juego()
        elif opcion == "2":
            mostrar_puntajes()
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


def main():
    menu()






