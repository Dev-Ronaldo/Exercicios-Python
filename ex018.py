#Exercicio 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
angulo=float(input('Digite um ângulo para saber seu seno, cosseno e tangente:'))

print('O ângulo escolhido foi: {}\nO Seno é: {:.2f}\nO cosseno é: {:.2f}\nA tangente é: {:.2f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
