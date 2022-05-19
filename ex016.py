#Exercicio 16 - Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex, digite 6,127 e mostre 6

from math import trunc
n = float(input('Digite um numero para saber sua porção inteira:'))
print('O numero escolhido é: {} e a sua porção inteira é: {}'.format(n, trunc(n)))
