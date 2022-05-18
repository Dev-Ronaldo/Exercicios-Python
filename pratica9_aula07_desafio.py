#Desafio 011 - Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la.
#sabendo que cada litro de tinta pinta uma area de 2m²

h=float(input('Digite a altura da parede:'))
l=float(input('Digite a largura da parede:'))
area= h * l
qtdtinta = area / 2

print('A área da parede é: {}m² \nQuantidade de tinta necessária: {:.2f} litros'.format(area, qtdtinta))
