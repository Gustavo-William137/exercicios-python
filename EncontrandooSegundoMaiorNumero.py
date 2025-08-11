num = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def imprimir(num): 
    unicos = list(set(num))
    unicos.sort(reverse=True)
    if len(unicos) < 2:
        print("Não há segundo maior número (lista com poucos valores únicos).")
    else:
        print(f'O segundo maior número encontrado foi: {unicos[1]}')

imprimir(num)
