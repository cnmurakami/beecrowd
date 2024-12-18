competidores, papel_total, papel_individual = input().split(" ")

competidores = int(competidores)
papel_total = int(papel_total)
papel_individual = int(papel_individual)

if papel_individual*competidores <= papel_total:
    print ("S")
else:
    print("N")