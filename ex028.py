#Exercicio 028 - Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuario venceu ou perdeu.
import random

numero=int(input('Digite um número inteiro entre 0 e 5:'))
numero2=random.randint(0,5)

if numero==numero2:
    print('Parabéns! Voce acertou!')
else:
    print('Você errou, o computador venceu!')
print('Você digtou {}\nO numero escolhido foi {}'.format(numero, numero2))