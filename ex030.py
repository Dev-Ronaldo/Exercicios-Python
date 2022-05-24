#Exercicio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

num=int(input('Digite um numero para verificar se é par ou impar:'))
div=num%2
if div==0:
    print('O numero escolhido foi {}! e ele é PAR'.format(num))
else:
    print('O numero escolhido foi {}! e ele é IMPAR'.format(num))