#Exercicio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

n=int(input('Digite um numero para calcular sua tabuada:'))
i=0
for i in range(0,11):   #utilizei estrutura de repetição for, pois já conhecia de outras linguagens.
    n1=n*i
    print('{} * {} = {}'.format(n, i, n1))