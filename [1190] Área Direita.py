'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área direita da matriz, conforme ilustrado abaixo (área verde).
   0 1  2 3  4 5  6 7  8 9 10 11
 0🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨
 1⬜🟨⬜⬜⬜⬜⬜⬜⬜⬜🟨🟩
 2⬜⬜🟨⬜⬜⬜⬜⬜⬜🟨🟩🟩
 3⬜⬜⬜🟨⬜⬜⬜⬜🟨🟩🟩🟩
 4⬜⬜⬜⬜🟨⬜⬜🟨🟩🟩🟩🟩
 5⬜⬜⬜⬜⬜🟨🟨🟩🟩🟩🟩🟩
 6⬜⬜⬜⬜⬜🟨🟨🟩🟩🟩🟩🟩
 7⬜⬜⬜⬜🟨⬜⬜🟨🟩🟩🟩🟩
 8⬜⬜⬜🟨⬜⬜⬜⬜🟨🟩🟩🟩
 9⬜⬜🟨⬜⬜⬜⬜⬜⬜🟨🟩🟩
10⬜🟨⬜⬜⬜⬜⬜⬜⬜⬜🟨🟩
11🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''

operacao = str(input())
matriz = [[]]
valor = 0
resultado = 0
quantidade = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)
    matriz.append([])
    

for i in range(12):
    k = 0
    for j in range (11, 0, -1):
        if j > i and k < i and j != i:
            resultado += matriz[i][j]
            quantidade += 1
            k += 1

if operacao == 'M':
    resultado = resultado / quantidade

print(f'{resultado:.1f}')