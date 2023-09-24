import pygame

preguntas = []
opcionesA =[]
opcionesB =[]
opcionesC =[]
correctas =[]
preguntas_respondidas = []
respuestaA = None
respuestaB = None
respuestaC = None
numero_colision = None
ternario = None
inicio_juego = False
termino = False
vidas = 2
puntos = 0
puntuacion = "Score:{0}"
mensaje_puntuacion = "Su puntuacion es de : {0} ".format(puntos)
lista_rect = [pygame.Rect(1030,30,200,70),pygame.Rect(1030,120,200,70)]

