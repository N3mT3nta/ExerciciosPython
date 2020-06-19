#Para IDE local:

'''import pygame
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

#Para Repl.it:

from replit import audio

audio.play('music.mp3')
input('Tocando...')
