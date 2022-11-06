from pessoa import Pessoa

p1 = Pessoa('Joana', 20)
print(p1.nome)

p1.comer("maçã")
print(p1.comendo)
p1.comer("laranja")

p2 = Pessoa("Renata", 24)
p2.parar_comer()

print(p1.ano_atual)
print(p2.ano_atual)

