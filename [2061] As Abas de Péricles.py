abas, acoes = input().split(" ")
abas,acoes = int(abas),int(acoes)

for i in range(acoes):
    acao = input()
    if acao == 'fechou':
        abas += 1
    else:
        abas -= 1

print(abas)
