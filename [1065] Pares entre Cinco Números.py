'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''
contagem = int(0)
valor = []

for i in range(5):
    valor.append(int(input()))

for i in range(5):
    if valor[i] % 2 == 0:
        contagem += 1

print(contagem, 'valores pares')