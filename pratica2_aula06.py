#Desafio 004 - Aula 06
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

n=input('Digite um valor:')
print(type(n))
print('é alfa numérico?',n.isalnum())
print('é alfabético?',n.isalpha())
print('está digitado apenas com letras minusculas?',n.islower())
print('está digitado apenas com letras maiusculas?',n.isupper())
print('é  valor numérico?',n.isnumeric())