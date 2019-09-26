#from pygame import mixer
import pygame

pygame.init()
mixer.init()
#mixer.music.load('musica.mp3')
#mixer.music.play()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

parar = input('Digite algo para parar...')