#Exercicio 026 - Faça um programa que leia uma frase pelo teclado e mostre: -Quantas vezes aparece a letra "A" - Em que posição ela aparece a primeira vez - Em que posição ela aparece a ultima vez

frase=str(input('Digite uma frase para contar a quantidade de letras "a":')).strip()  #.strip() = remoção dos espaços

print('Aparecem {} vezes a letra "a" na frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.lower().find('a')+1))  #o +1 indica exatamente a posição, pois o contador se inicia em 0
print('A ultima letra A apareceu na posição: {}'.format(frase.lower().rfind('a')+1)) #rfind indica que a pesquisa começa pelo lado direito da frase
