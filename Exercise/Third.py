import json

with open("dados.json", encoding='utf-8') as my_json:
    dados = json.load(my_json)
#print(dados)


total_dias = len(dados)
soma = sum(c['valor'] for c in dados)
media = soma/total_dias

min_fat = dados[0]['valor']
max_fat = dados[0]['valor']
max_day = 0
soma_fat = 0
count_fat = 0
for day in dados:
    if day['valor'] > max_fat:
        max_fat = day['valor']
        max_day = day['dia']
    if day['valor'] < min_fat:
        min_fat = day['valor']
    if day['valor'] > media:
        count_fat = count_fat + 1



print('DIAS ACIMA DA MÉDIA: ',count_fat)
print('MENOR VALOR DE FATURAMENTO: ',min_fat)
print('MAIOR VALOR DE FATURAMENTO: ',max_fat)
print('      DIA DO MAIOR FATURAMENTO: ',max_day)