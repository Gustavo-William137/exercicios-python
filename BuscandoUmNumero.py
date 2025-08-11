num = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def imprimir(num, valor): 
    encontrado = valor in num
    print(f'O número {valor} está na lista? {encontrado}')

imprimir(num, 42)   
imprimir(num, 12345)  
