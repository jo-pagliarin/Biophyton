dic = {} # Inicializa ou reinicializa um dicionário existente
dic = {'5GJA:A':61, '5GJ4:B':177, '5GJ4:C':61, '5GJK:D':177, '5GP1:B':268}

dic['XXX'] = 999
# Uma nova chave será criada no dicionário caso ainda não exista
# O valor será atualizado caso já exista

print(dic['5GJA:A']) # Imprime 61
print(dic['5GJ4:B']) # Imprime 177
print(dic['5GP1:B']) # Imprime 268

print('5GJ4:C' in dic)

dic2 = {'5GJA:A': 61, '5GJ4:B': 177, '5GJ4:C': 61, '5GJK:D': 177, '5GP1:B':268, '1A6M:A': 252, '2MM1:A': 251}
max(dic2) # Retorna “1A6M:A”
min(dic2) # Retorna “5GP1:B”

dic2.popitem() # remove um item aleatório
print(dic2)

# ENDEREÇO DE MEMÓRIA
print(id(dic)) # 1456311977600
print(id(dic2)) # 1456311977344

dic2 = dic
print(id(dic2)) # 1456311977600


a = {'A': 1, 'B': 2, 'C': 3}
b = {'A': 4, 'D': 5, 'C': 7}
b = a # isso faz com que todas as alterações feitas em "a" se reflita em "b"
print(b)

a['E'] = 8
print(a)
print(b)

c = a.copy()
print(c)
print(id(a))
print(id(c))
# valores diferentes 
a['C'] = 8
print(a)
print(c)
# só altera em "a"

print(c.keys())
print(list(c.keys())[0])
print(c.values())
print(c.items())

listC = list(c)
print(listC)
print(type(listC))

# Convertendo listas em dicionários
# O método zip() retorna uma lista contendo tuplas, onde o primeiro valor é o da primeira lista, e o segundo valor da tupla, corresponde a segunda lista
firstList = ["joana", "roberta", "patricia"]
secondList = ["pagliarin", "silva", "matias"]
newDict = list(zip(firstList, secondList))
print(newDict)
# saída: [('joana', 'pagliarin'), ('roberta', 'silva'), ('patricia', 'matias')
print(type(newDict))
# saída: list
newDict = dict(newDict) # prestar atenção nas chaves
print(newDict)
# saída: {'joana': 'pagliarin', 'roberta': 'silva', 'patricia': 'matias'} 
print(type(newDict))
# saída: dict



