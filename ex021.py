#Exercicio 021 - Faça um programa em python que abra e reproduza um áudio de um arquivo mp3.

import pygame
pygame.mixer.init() #
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0,start=0) #nesta linha podemos ter contador de loops e com quantos segundos a musica começa
pygame.mixer.music.set_volume(0.1) #ajusta o volume de inicio da musica

volume=int(input('digite o valor do volume que deseja de 0 a 100:')) #recebendo um valor para alteração de volume
volume2=volume/100
pygame.mixer.music.set_volume(volume2) #comando que recebe a variável para ajuste de volume

pygame.event.wait()

#a musica não foi inserida nos arquivos do github devido possibilidade de direitos autorais
