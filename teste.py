import json
from tabelas import arquivo as arq

times = list()
times.append({"time": "Palmeiras", "jogos": "30", "pontos": "61"})
times.append({"time": "São Paulo", "jogos":"31", "pontos":"50"})

#times = {"time": "palmeiras"}
teste = arq('brasil.txt', times, True)
if teste: print(teste)
