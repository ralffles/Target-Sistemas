import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

# Menor valor de faturamento
menor_faturamento = min(d['valor'] for d in dados)
print(f'Menor valor de faturamento: {menor_faturamento:.2f}')

# Maior valor de faturamento
maior_faturamento = max(d['valor'] for d in dados)
print(f'Maior valor de faturamento: R${maior_faturamento:.2f}')

# Média mensal de faturamento
media_faturamento = sum(d['valor'] for d in dados) / len(dados)

# Número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(d['valor'] > media_faturamento for d in dados)
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')