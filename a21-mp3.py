import random
import pygame

pygame.init()

pygame.mixer.music.load('mp3/game.mp3')
pygame.mixer.music.play()
# input("Tocando... Tecle enter para parar.")

mp3 = ['game', 'funny-bgm', 'space-station', 'stranger-things', 'this-8-bit-music']

sair = ""
while(sair != "s"):
    tocar = random.choice(mp3)
    titulo = tocar.split("-")
    titulo = " ".join(titulo).title()

    pygame.mixer.music.load(f'mp3/{tocar}.mp3')
    pygame.mixer.music.play()
    sair = input(f'Tocando "{titulo}".'
                 f'\nTecle enter para tocar outra música aleatória.'
                 f'\nDigite "s" para sair: ').lower().strip()
    print()

print("Bye bye...")
