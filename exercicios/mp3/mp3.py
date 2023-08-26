"""O som infelizmente não funciona todas vezes. Em breve usarei outro aquivo
de audio mais trabalhado para esse programa"""

import pygame

pygame.init()
pygame.mixer.music.load('exercicios/mp3/ride.wav')
pygame.mixer.music.play()
pygame.event.wait()