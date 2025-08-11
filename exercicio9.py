num = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def imprimir(num, valor):
    quantidade = num.count(valor)
    print(f'O número {valor} aparece {quantidade} vez(es) na lista.')

imprimir(num, 2)
imprimir(num, 13)
