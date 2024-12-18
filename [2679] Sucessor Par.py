"""
Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

Entrada
Uma linha contendo um número  0 < X < 107.

Saída
Uma linha contendo a resposta do problema.
"""

entrada = int(input())
if (entrada+1) % 2 == 0:
    print (entrada+1)
else:
    print(entrada+2)