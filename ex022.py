#Exercicio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#Nome com todas letras maiusculas
#Nome com todas letras minusculas
#Quantas letras no total sem considerar espaços
#Quantas letras tem o primeiro nome

nome=str(input('Digite seu nome completo:')).strip()

print('seu nome em letras maiusculas é:', nome.upper())
print('seu nome em letras minusculas é:', nome.lower())
print('A quantidade de letras que seu nome possui é:', len(nome) - nome.count(' '))
nomeseparado = nome.split()
print('Seu primeiro nome tem {} letras!' .format(len(nomeseparado[0])))

#Tambem pode ser feito de outra forma encontrando o primeiro espaço e mostrando a posição
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))