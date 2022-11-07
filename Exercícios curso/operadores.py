# EXERCÍCIO 1
a = 5
b = 3
print(a==b)

# EXERCÍCIO 2
c = 2
d = 23
e = 4
f = 2
g = 1
print((c+d+e+f+g)/5)

# EXERCÍCIO 3
base = 2
expoente = 4
print(pow(base,expoente))

# EXERCÍCIO 4
x = 8
y = 3
if(x%y == 0):
    print("x é divísivel por y")
else:
    print("não é divísivel")
    
# EXERCÍCIO 5
print(x//y)

# EXERCÍCIO 6 e 7
numero = 30
if numero in range(5,30): # 5 é intervalo fechado, 30 é intervalo aberto
    print(f'{numero} pertence ao intervalo [5,30]')

# EXERCÍCIO 8
lista =  ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
letra = 'Z'
if letra in lista:
    print(f'{letra} pertence a lista de aminoácidos')
    
# EXERCÍCIO 9
pos = ['H', 'K', 'R']
neg = ['D', 'E']
# dado um aminoácido, determinar se é carregado ou neutro
aminoacido = "E"
if aminoacido in pos or aminoacido in neg:
    print(f'{aminoacido} é carregado')
else:
    print(f'{aminoacido} é neutro')
