numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def remover_duplicatas(lista):
    return list(set(lista))

unicos = remover_duplicatas(numeros)
print(f'Lista com valores únicos: {unicos}')