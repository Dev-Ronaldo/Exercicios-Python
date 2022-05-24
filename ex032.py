#Exercicio 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano=int(input('Digite um ano para verificar se é bissexto (DIGITE 0 PARA VERIFICAR O ANO ATUAL):'))
if ano==0:
    ano=date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('o ano {} não é bissexto!'.format(ano))
