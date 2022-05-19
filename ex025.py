#Exercicio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome=str(input('Digite um nome para verificar:')).strip()

#print('Seu nome tem silva? {}'.format(nome[:6].lower() == 'silva')) ---> verifica somente um nome

print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
