import pygame
import pygame.mixer as mixer
import sys
import random
import json
import os
import time
from config import CELDAS, ANCHO, ALTO,FONDO, FILAS, COLUMNAS, NEGRO, BLANCO, ROJO, FUENTE, INPUTBOX, BOTONRECT
from funciones_candy import generar_matriz, mostrar_puntajes, guardar_puntaje_json, verificar_tres_juntos


#inicializacion
pygame.init()

#creo ventana principal(elijo la resolucion)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Candy Crush") #titulo
icono = pygame.image.load("Funcionamiento/archivos/icono_candy.jpg")
pygame.display.set_icon(icono)

#cargo piezas  
pieza1 = pygame.image.load("Funcionamiento/archivos/cotton_candy.png")  
pieza2 = pygame.image.load("Funcionamiento/archivos/pop_candy.png")
pieza3 = pygame.image.load("Funcionamiento/archivos/waffle_candy.png")

#las ajusto a las celdas
pieza1 = pygame.transform.scale(pieza1, (CELDAS, CELDAS))
pieza2 = pygame.transform.scale(pieza2, (CELDAS, CELDAS))
pieza3 = pygame.transform.scale(pieza3, (CELDAS, CELDAS))
FUENTE = pygame.font.Font("Funcionamiento/archivos/Happy Monday.ttf", 70)
#musica
pygame.mixer.music.load("Funcionamiento/archivos/Dance of the Hours.mp3") 
mixer.music.set_volume(0.3)
pygame.mixer.music.play()






def dibujar_matriz(matriz):
    for i, fila in enumerate(matriz):
        for j, pieza in enumerate(fila["piezas"]):        #creo matriz y acomodo depende el numero a la pieza que puse
            
            if pieza == 1:
                pantalla.blit(pieza1, (j * CELDAS, i * CELDAS))
            elif pieza == 2:
                pantalla.blit(pieza2, (j * CELDAS, i * CELDAS))
            elif pieza == 3:
                pantalla.blit(pieza3, (j * CELDAS, i * CELDAS))

    for i in range(FILAS + 1):   #bordes
        pygame.draw.line(pantalla, NEGRO, (0, i * CELDAS), (ANCHO, i * CELDAS), 2)
    for j in range(COLUMNAS + 1): #bordes x2
        pygame.draw.line(pantalla, NEGRO, (j * CELDAS, 0), (j * CELDAS, ALTO), 2)

def mostrar_texto(texto, color, x, y):
    texto_renderizado = FUENTE.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))


def dibujar_botones():
    # Botón Play
    pygame.draw.rect(pantalla, BLANCO, (300, 200, 200, 50))
    mostrar_texto("Jugar", NEGRO, 375, 210)

    # Botón Puntajes
    pygame.draw.rect(pantalla, BLANCO, (300, 300, 200, 50))
    mostrar_texto("Puntajes", NEGRO, 350, 310)

    # Botón Opciones
    pygame.draw.rect(pantalla, BLANCO, (300, 400, 200, 50))
    mostrar_texto("Salir", NEGRO, 350, 410)


def dibujar_puntajes():

    imagen_puntajes = pygame.image.load("Funcionamiento/archivos/Puntajes mickey.png")
    imagen_puntajes = pygame.transform.scale(imagen_puntajes, (ANCHO, ALTO))
    pantalla.blit(imagen_puntajes, (0, 0))

    mostrar_texto("Puntajes:", BLANCO, 350, 50)

    if os.path.exists("puntajes.json"):  # Asegúrate de que se lea del archivo correcto
        with open("puntajes.json", "r") as file:
            scores = json.load(file)
        
        if scores:
            scores.sort(key=lambda x: x['nombre'].lower()) #ordeno alfabeticamente y pongo lower por las minusculas
            y_offset = 100
            for score in scores:
                mostrar_texto(f"{score['nombre']}: {score['puntaje']} puntos", NEGRO, 300, y_offset)
                y_offset += 40
        else:
            mostrar_texto("Empty .", ROJO, 150, 150)
    
    pygame.display.update()


def mostrar_menu():
    imagen_menu = pygame.image.load("Funcionamiento/archivos/Fondo inicio.jpg")
    imagen_menu = pygame.transform.scale(imagen_menu, (ANCHO, ALTO))
    pantalla.blit(imagen_menu, (0, 0))       
    
    mostrar_texto("Menu", BLANCO, 350, 50)
    mostrar_texto("1. Play", BLANCO, 350, 150)             #texto sobre img
    mostrar_texto("2. Scores", BLANCO, 350, 200)
    mostrar_texto("3. Quit", BLANCO, 350, 250)

    pygame.display.update()


def jugar():
    matriz = generar_matriz(FILAS, COLUMNAS)
    puntaje = 0
    tiempo_restante = 10
    nombre_jugador = ""
    color_input = (255, 255, 255)  # cuadro texto
    active = False  #estado del cuadro
    clock = pygame.time.Clock()

    pantalla.fill(FONDO)
    mostrar_texto("Name:", BLANCO, 200, 80)
    pygame.display.update()

    # Iniciar el bucle de entrada de texto para el nombre
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if INPUTBOX.collidepoint(evento.pos): 
                    active = True  # click para escribir
                else:
                    active = False  #click fuera off

            if evento.type == pygame.KEYDOWN:
                if active:
                    if evento.key == pygame.K_RETURN: 
                        if nombre_jugador: 
                            return correr(nombre_jugador)  # inicio con enter
                    elif evento.key == pygame.K_BACKSPACE:  # borro
                        nombre_jugador = nombre_jugador[:-1]  
                    else:
                        nombre_jugador += evento.unicode  # lo que escribo va al nombre


        pygame.draw.rect(pantalla, color_input, INPUTBOX) 
        mostrar_texto(nombre_jugador, NEGRO, INPUTBOX.x + 5, INPUTBOX.y + 5)         # Dibujo el cuadro de texto y mostrarmuestro el texto ingresado
        pygame.display.update()  


def correr(nombre_jugador):
    matriz = generar_matriz(FILAS, COLUMNAS)
    puntaje = 0
    tiempo_restante = 10
    tiempo_inicial = time.time()
    mensaje_error = ""  
    tiempo_error = 0  
    corriendo = True

    while corriendo and tiempo_restante > 0:
        tiempo_restante = 10 - int(time.time() - tiempo_inicial)

        pantalla.fill(FONDO)
        dibujar_matriz(matriz)
        mostrar_texto(f"Score: {puntaje}", NEGRO, 10, 10)
        mostrar_texto(f"Time: {max(0, tiempo_restante)}s", NEGRO, 450, 10)

        if mensaje_error and pygame.time.get_ticks() - tiempo_error < 1000:           #me muestra el oerror por 1 s
            mostrar_texto(mensaje_error, ROJO, 250, 150)

        pygame.display.update()


        if tiempo_restante <= 0:
            corriendo = False
            guardar_puntaje_json(nombre_jugador, puntaje)                                                     #tiempo 0 termina el juego, muestro puntaje y esp
            pantalla.fill(FONDO)
            mostrar_texto(f"Game over! {nombre_jugador}, your score is: {puntaje}", ROJO, 50, 250)
            pygame.display.update()
            time.sleep(2)
            return "menu"  #menu o go

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:        #crucesita
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                columna = x // CELDAS
                fila = y // CELDAS

                if verificar_tres_juntos(matriz, fila, columna):
                    puntaje += 10  
                    mensaje_error = ""  #saco el mensaje de error si sumo bien
                else:
                    tiempo_restante -= 1 
                    puntaje -= 1  
                    mensaje_error = "¡-Time!"  
                    tiempo_error = pygame.time.get_ticks()  
                matriz = generar_matriz(FILAS, COLUMNAS) #regenero matriz despues de cada intento

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            corriendo = False  
            return "menu"  # esc menu

    return "menu"  


def main():
    if not os.path.exists("puntajes.json"):
        with open("puntajes.json", "w") as archivo:
            json.dump([], archivo)  # me fijo si esta el json sino lo creo

    estado = "menu"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:      #crucesita
                    pygame.quit()
                    quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  #posicion click

                # Verificar clics en botones
                if 350 <= x <= 450 and 150 <= y <= 200:  # jugar
                    estado = jugar()
                elif 350 <= x <= 450 and 200 <= y <= 250:  # ver Puntajes
                    estado = "puntajes"
                elif 350 <= x <= 450 and 250 <= y <= 300:  # salir
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                if estado == "jugando":  # esc para menu
                    estado = "menu"
        
        if estado == "menu":
            mostrar_menu()

        elif estado == "puntajes":
            dibujar_puntajes()

            keys = pygame.key.get_pressed()  #esc otra ve
            if keys[pygame.K_ESCAPE]:
                estado = "menu"
                    
        pygame.display.update()


        


if __name__ == "__main__":
    main()



