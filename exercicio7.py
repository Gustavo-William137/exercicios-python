class Pessoa:
    def __init__(self, nome):
        self.nome = nome

objetos = [
    Pessoa("Ana"),
    Pessoa("João"),
    Pessoa("Carlos"),
    Pessoa("Maria")
]

def imprimir(objetos):
    nomes = [obj.nome for obj in objetos]
    print(f'Nomes encontrados: {nomes}')

imprimir(objetos)
