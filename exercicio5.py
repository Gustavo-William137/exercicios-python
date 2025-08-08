from time import sleep

opçao = 0
while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('===' * 20)
    sleep(1)
    print(''' Calculadora Massa
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Sair''')

    opçao = int(input('>>> Qual a opção desejada: '))
    if opçao == 1:
        soma  = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    if opçao == 2:
        subtraçao = n1 - n2
        print(f'A subtração entre {n1} - {n2} = {subtraçao}')
    if opçao == 3:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = {multiplicação}')
    if opçao == 4:
        divisao = n1 / n2
        print(f'A divisão de {n1} / {n2} = {divisao}')
    else:
        print('FINALIZANDOOOOOO...')
        sleep(1)
        break

   
   