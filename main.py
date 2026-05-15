temperatura = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior = 0
sala = 0

for i in range(len(temperatura)):
    soma = 0
    criticos = 0

    for temp in temperatura[i]:
        soma += temp
        if temp >= 33:
            criticos += 1

    media = soma / len(temperatura[i])

    print(f"Sala {i + 1} \n Média: {media} \n Registros críticos: {criticos}")

    if criticos > maior:
        maior = criticos
        sala = i + 1

print()
print(f"Sala com maior risco: Sala {sala}")