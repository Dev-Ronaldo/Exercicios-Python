#Exercicio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade=str(input('Digite o nome de uma cidade:')).strip() #removendo espaços com .strip()

print(cidade[0:5].lower() == 'santo') #transformando tudo para letra minuscula para verificar a palavra independente da forma que o usuario digite
