'''
O jogo de Sudoku espalhou-se rapidamente por todo o mundo, tornando-se hoje o passatempo mais popular em todo o planeta. Muitas pessoas, entretanto, preenchem a matriz de forma incorreta, desrespeitando as restrições do jogo. Sua tarefa neste problema é escrever um programa que verifica se uma matriz preenchida é ou não uma solução para o problema.

A matriz do jogo é uma matriz de inteiros 9 x 9 . Para ser uma solução do problema, cada linha e coluna deve conter todos os números de 1 a 9. Além disso, se dividirmos a matriz em 9 regiões 3 x 3, cada uma destas regiões também deve conter os números de 1 a 9. O exemplo abaixo mostra uma matriz que é uma solução do problema.



Entrada
São dadas várias instâncias. O primeiro dado é o número n > 0 de matrizes na entrada. Nas linhas seguintes são dadas as n matrizes. Cada matriz é dada em 9 linhas, em que cada linha contém 9 números inteiros.

Saída
Para cada instância seu programa deverá imprimir uma linha dizendo "Instancia k", onde k é o número da instância atual. Na segunda linha, seu programa deverá imprimir "SIM" se a matriz for a solução de um problema de Sudoku, e "NAO" caso contrário. Imprima uma linha em branco após cada instância.
'''

def monta_jogo():
    jogo = []
    for linha in range(9):
        jogo.append(input().split(" "))
    for linha in range(len(jogo)):
        for coluna in range(len(jogo[linha])):
            jogo[linha][coluna] = int(jogo[linha][coluna])
    return jogo

def verifica_linha(jogo):
    for i in range(len(jogo)):
        for j in range (len(jogo[i])):
            if jogo[i].count(j) > 1:
                return False
    return True

def verifica_coluna(jogo):
    teste = []
    for linha in range(len(jogo)):
        teste.append([])
        for coluna in range (len(jogo[linha])):
            teste[linha].append(jogo[coluna][linha])
    return verifica_linha(teste)

def verifica_matriz(jogo):
    teste = []
    linhas = [(0, 3), (3, 6), (6, 9)]

    for linha in range(0,len(jogo)):
        teste.append([])
    
    for i in range(len(linhas)):
        for j in range(linhas[i][0], linhas[i][1]):
            for k in range(len(linhas)):
                for l in range(linhas[k][0], linhas[k][1]):
                    teste[linhas[i][0] + k].append(jogo[j][l])
    return verifica_linha(teste)



#__main__
qtd = int(input())
instancia = []
testes = []

for i in range(qtd):
    instancia.append(monta_jogo())
    testes.append({'linha':True, 'coluna':True, 'matriz':True})

for id in range(len(instancia)):
    testes[id]['linha'] = verifica_linha(instancia[id])
    testes[id]['coluna'] = verifica_coluna(instancia[id])
    testes[id]['matriz'] = verifica_matriz(instancia[id])

for i in range(qtd):
    print ('Instancia', i + 1)
    if testes[i]['linha'] and testes[i]['coluna'] and testes[i]['matriz']:
        print('SIM\n')
    else:
        print('NAO\n')
