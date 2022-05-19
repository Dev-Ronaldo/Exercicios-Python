#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome=str(input('Digite seu nome completo":')).strip()
nomedividido=nome.split()

print('Seu primeiro nome é: {}'.format(nomedividido[0]))
print('Seu ultimo nome é: {}'.format(nomedividido[len(nomedividido)-1]))