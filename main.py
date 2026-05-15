temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_criticos = 0
sala_maior_risco = 0

for i in range(len(temperaturas)):
    soma = 0
    criticos = 0

    for temp in temperaturas[i]:
        soma += temp
        if temp >= 33:
            criticos += 1

    media = soma / len(temperaturas[i])

    print(f"Sala {i + 1} Média: {media} Registros críticos: {criticos}")

    if criticos > maior_criticos:
        maior_criticos = criticos
        sala_maior_risco = i + 1

print(f"\nSala com maior risco: Sala {sala_maior_risco}")