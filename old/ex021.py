'''from playsound import playsound
print('Playing...')
playsound('C:/Users/Samuel/Desktop/Scripts/ExerciciosPython/ex021.mp3')'''

import pygame
pygame.mixer.init()
goblins = str('ex021.mp3')
pygame.mixer.music.load(goblins)
pygame.mixer.music.play()
input('Playing...')

'''#Code from Repl.it
import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=1)
input('Digite algo para interromper:')'''
