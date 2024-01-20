'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

n = []
maior = 0
posicao = 0
for i in range(0, 100):
    test = int(input())
    n.append(test)
    if test > maior:
        maior = test
        posicao = i + 1
print(maior)
print(posicao)