import pygame
import random

import colores
from constantes import *
from variables import *
from datos import lista

def logica_pregunta(numero_pregunta,respuesta,):
    if respuesta == correctas[numero_pregunta]:
        preguntas_respondidas.append(numero_pregunta)
        sonido_correcto.play()
        return elegir_pregunta(preguntas_respondidas)
    else:
        sonido_incorrecto.play()
        return -1
    

def elegir_pregunta(preguntas_respondidas):
    while True:
        repetido = False
        numero_pregunta = random.randint(0,(len(preguntas))-1)
        if len(preguntas_respondidas) == len(preguntas):
            return True
        for pegunta_numero in preguntas_respondidas:
            if numero_pregunta == pegunta_numero:
                repetido = True
        if not(repetido):
            return numero_pregunta 









for elemento in lista:
    preguntas.append(elemento["pregunta"])
    opcionesA.append(elemento["a"])
    opcionesB.append(elemento["b"])
    opcionesC.append(elemento["c"])
    correctas.append(elemento["correcta"])

pregunta_actual = elegir_pregunta(preguntas_respondidas)
pygame.init
corriendo = True

logo_peguntados = pygame.image.load(UBI_IMAGENES + "logo.png")
pygame.font.init()
fuente = pygame.font.Font(None,30)
titulo = pygame.font.Font(None,50)


pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Preguntados")


pygame.mixer.init()

sonido_correcto = pygame.mixer.Sound(UBI_SONIDOS + "Sonido-de-correcto-de-Preguntados.mp3")
sonido_incorrecto = pygame.mixer.Sound(UBI_SONIDOS + "Sonido-de-incorrecto-de-Preguntado.mp3")

sonido_correcto.set_volume(0.5)
sonido_incorrecto.set_volume(0.5)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                rect_mouse = pygame.Rect(pos_mouse[0],pos_mouse[1],4,4)
                numero_colision = pygame.Rect.collidelist(rect_mouse,lista_rect)
            
    match(numero_colision):
        case 0:
            if inicio_juego and not(termino):
                preguntas_respondidas.append(pregunta_actual)
                elegir_pregunta(preguntas_respondidas)
            elif not(termino):
                inicio_juego = True 
        case 1:
            elegir_pregunta(preguntas_respondidas)
            preguntas_respondidas = []
            puntos = 0
            inicio_juego = False
            termino = False
        case 2:
            ternario = logica_pregunta(pregunta_actual,"a")
        case 3:
            ternario = logica_pregunta(pregunta_actual,"b")
        case 4:
            ternario = logica_pregunta(pregunta_actual,"c")
    
    
    if type(ternario) == int:
        if ternario == -1:
            vidas -= 1
            if vidas == 0:
                preguntas_respondidas.append(pregunta_actual)
                pregunta_actual = elegir_pregunta(preguntas_respondidas)
        else:
            puntos += 10
            vidas = 2
            pregunta_actual = ternario
    elif (ternario):
        puntos += 10
        inicio_juego = False
        termino = True
        
    ternario = None
    numero_colision = None

    pygame.Surface.fill(pantalla,colores.GRAY15)

    pygame.Surface.blit(pantalla,logo_peguntados,(0,0))
    
    
    score = fuente.render(puntuacion.format(puntos),0,colores.WHITESMOKE)
    pygame.Surface.blit(pantalla,score,POS_SCORE)

    boton_inicio = pygame.draw.rect(pantalla,colores.YELLOW1,lista_rect[0])
    inicio_txt = fuente.render("preguntar",0,colores.BLACK)
    pygame.Surface.blit(pantalla,inicio_txt,POS_BOTON_INICIO)


    
    boton_reinicio = pygame.draw.rect(pantalla,colores.YELLOW1,lista_rect[1])
    reiniciar = fuente.render("reiniciar",0,colores.BLACK)
    pygame.Surface.blit(pantalla,reiniciar,POS_BOTON_REINICIO)


    if inicio_juego:
        pregunta = fuente.render(preguntas[pregunta_actual],0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,pregunta,POS_PREGUNTA)

        respuestaA = fuente.render(opcionesA[pregunta_actual],0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,respuestaA,POS_RESPUESTA_A)

        respuestaB = fuente.render(opcionesB[pregunta_actual],0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,respuestaB,POS_RESPUESTA_B)

        respuestaC = fuente.render(opcionesC[pregunta_actual],0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,respuestaC,POS_RESPUESTA_C)

        if len(lista_rect) == 2:
            for cantidad_respuestas in range(3):
                lista_rect.append("")
        lista_rect[2] = respuestaA.get_rect()
        lista_rect[2].move_ip(POS_RECT_OPCION_A)
        lista_rect[3] = respuestaB.get_rect()
        lista_rect[3].move_ip(POS_RECT_OPCION_B)
        lista_rect[4] = respuestaC.get_rect()
        lista_rect[4] .move_ip(POS_RECT_OPCION_C )

    if termino :
        mensaje_felicitacion = "Felicitaciones a respondido a todas las preguntas."
        mensaje_puntuacion = "Su puntuacion es de : {0} ".format(puntos) 

        felicitacion = titulo.render(mensaje_felicitacion,0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,felicitacion,POS_FELICITACION)

        puntuacion_final = titulo.render(mensaje_puntuacion,0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,puntuacion_final,POS_PUNTUACION_FINAL)
    pygame.display.flip()

pygame.quit

