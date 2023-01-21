# EXERCÍCIO 1
def imprimeNumerosFor():
    numeros = []
    for i in range(0,11):
        numeros.append(i)
    print(numeros)
    
def imprimeNumerosWhile():
    numeros = []
    i = 0
    while i <= 10:
        numeros.append(i)
        i = i + 1
    print(numeros)

# imprimeNumerosFor()
# imprimeNumerosWhile()

# EXERCÍCIO 2
def imprimeNumerosFor2():
    numeros = []
    for i in range(0,11,2):
        numeros.append(i)
    print(numeros)
    
def imprimeNumerosWhile2():
    numeros = []
    i = 0
    while i <= 10:
        if i%2 == 0:
            numeros.append(i)
        i = i + 1
    print(numeros)

# imprimeNumerosFor2()
# imprimeNumerosWhile2()

# EXERCÍCIO 3
seqA = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
def verifica(seqA):
    for base in seqA:
        if base == 'U':
            print("A sequência é de RNA")
            return
    print("A sequência é de DNA")
        
# verifica(seqA)

# EXERCÍCIO 4 
def imprimeDivisores():
    for i in range(1,101):
        for j in range(1,10):
            if i%j == 0:
                print(f'{i} é divisível por {j}')

# imprimeDivisores()

# EXERCÍCIO 5
def imprimePrimos():
    naoPrimos = []
    primos = []
    for i in range(1,51):
        for j in range(2, i):
            if i%j == 0:
                try:
                    naoPrimos.index(i)
                except:
                    naoPrimos.append(i)
    print(naoPrimos)
    for k in range(2,51):
        try:
            naoPrimos.index(k)
        except:
            primos.append(k)
    print(primos)


def codigoProf():
    for n in range(1,51): # Percorrer os 100 números
        div = []
        for d in range(1,n+1): # Percorrer os n possíveis divisores de um número
            if n%d == 0:  
                div.append(d)  
        if len(div) == 2:
            print(n, end=" ")

# codigoProf()
# print("\n")
# imprimePrimos()

# EXERCÍCIO 6 
seq = "VRSSSRTPSDKPVAAAAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLAAAFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKAAASPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAAAAEINRPDYLLFAESGQVYFGIIAL"

def buscaAAA():
    for i in range(0,len(seq)):
        if seq[i:i+3] == "AAA":
            print("AAA em", i) 

# buscaAAA()

# EXERCÍCIO 7 
dicionario = {
    'A' : 'KTCENLA',
    'B' :  'DTFR',
    'C' : 'GPCFTDGSC',
    'D' : 'DDHCKNKEHLIK',
    'E' : 'GRCRDDFRC',
    'F': 'WCTRNC', 
    'G' : 'ATC'
}

dicionarioList = list(dicionario.values())

def buscaMaiorSeq():
    maiorTam = 0
    maiorIndice = 0
    for i in range(len(dicionarioList) - 1):
        if len(dicionarioList[i]) > maiorTam:
            maiorTam = len(dicionarioList[i])
            maiorIndice = i
    print(maiorTam)
    print(maiorIndice)
    print(dicionarioList[maiorIndice])
    print(list(dicionario.keys())[maiorIndice])
        
# buscaMaiorSeq()

# EXERCÍCIO 8 
lista = [1,4,6,3,4,5,7,8,9,5,6,7,4,3,5,6,7,8]
def calculaMedia():
    soma = 0
    for numero in lista:
        soma = soma + numero
    print(round(soma/len(lista),2))    
    
# calculaMedia()       