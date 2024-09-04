faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

dict_porcentagem = {}

soma_faturamentos = sum(faturamentos.values())

for key, value in faturamentos.items():
    dict_porcentagem[key] = str(round(value/soma_faturamentos*100, 2)) + '%'

print(dict_porcentagem)
