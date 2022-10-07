class Produto: 
    def __init__(self, nome, valor): 
        self.nome = nome 
        self.valor = valor 

chocolate = Produto("Chocolate", 4.35) 
refrigerante = Produto("Refrigerante", 3.75) 
feijao = Produto("Feijao", 10.5) 

produtos = [chocolate, refrigerante, feijao]

print(chocolate.nome, chocolate.valor)
