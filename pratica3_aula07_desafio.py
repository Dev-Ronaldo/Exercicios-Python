#Desafio 005 - Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor

n1=int(input('digite um numero para verificar seu sucessor e antecessor:'))
print('O numero digitado é: {} \nSeu sucessor é: {} \nSeu antecessor é: {}'.format(n1,n1+1,n1-1))