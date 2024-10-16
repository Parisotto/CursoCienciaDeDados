import random
import pygame

pygame.init()
pygame.mixer.music.load('game.mp3')
pygame.mixer.music.play()
# input("Tocando... Tecle enter para parar.")

mp3 = ['game', 'funny-bgm', 'space-station', 'stranger-things', 'this-8-bit-music']

tocar = random.choice(mp3)
titulo = tocar.split("-")
titulo = " ".join(titulo).title()

pygame.mixer.music.load(f'{tocar}.mp3')
pygame.mixer.music.play()
input(f'Tocando "{titulo}"')
print("Bye bye...")
