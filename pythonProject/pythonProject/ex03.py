import json

with open('dados.json', 'r') as file:
    data = json.load(file)

    # Não foi inicializado em 0 para tratar faturamentos negativos
    menor_faturamento = data[0]['valor']
    maior_faturamento = data[0]['valor']

    media_mensal = sum([item['valor'] for item in data])/len(data)
    maior_que_media = 0
    for faturamento in data[1:]:
        if faturamento['valor'] > maior_faturamento:
            maior_faturamento = faturamento['valor']
        if faturamento['valor'] < menor_faturamento:
            menor_faturamento = faturamento['valor']
        if faturamento['valor'] > media_mensal:
            maior_que_media += 1

    print("O menor faturamento no mês foi de ", menor_faturamento)
    print("O maior faturamento no mês foi de ", maior_faturamento)
    print("A quantidade de faturamentos maior que a média ", media_mensal, " foi de ", maior_que_media)



