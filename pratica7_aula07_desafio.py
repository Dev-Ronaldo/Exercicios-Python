#Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

n=int(input('Digite um numero para calcular sua tabuada:'))
i=0
for i in range(0,11):   #utilizei estrutura de repetição for, pois já conhecia de outras linguagens.
    n1=n*i
    print('{} * {} = {}'.format(n, i, n1))

#de uma forma mais básica, pode-se resolver:
#print('Os valores obtidos da tabuada são: \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{}'.format(n*0, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))