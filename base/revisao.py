# Sintaxe básica
print("oi")

def soma(a,b):
    c = a+b
    print(c)
    
soma(3,5)

str1 = "Marrie "
str2 = "Currie"
str3 = "!!!"
print(str1 + str2 + str3)

def juntaStrings(*str):
    frase = ""
    for palavra in str:
        frase += palavra + " "
    print(frase)
    

juntaStrings("joana", "pagliarin", "é", "linda")

# Strings
str = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

print(len(str))
def contaTamSeq(str):
    count = 0
    i = 0
    while i < len(str):
        count += 1
        i +=1 
    return count    

tam = contaTamSeq(str)
print(tam)


print(str.count("LL"))
def contaLeucinas(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == "L":
            if str[i+1] == "L":
                count += 1
                i += 1
    print(count)
    
contaLeucinas(str)

# INDEX só retorna a primeira ocorrência daquela repetição
print(str.index("GG"))
def indicaPosGlicina(str):
    v = []
    for i in range(len(str) - 1):
        if str[i] == "G":
            if str[i+1] == "G":
                v.append(i)
    return v
                
print(indicaPosGlicina(str))

print(str.index("RR"))
def indicaPosArginina(str):
    v = []
    for i in range(len(str) - 1):
        if str[i] == "R":
            if str[i+1] == "R":
                v.append(i)
    return v

print(indicaPosArginina(str))


str2 = "aaaaGGaaaaGGaaaGGaaaaRRaaaRRGG"
print(str2.index("GG"))
def indicaIndexGlicina(str2):
    v = []
    for i in range(len(str2) - 1):
        if str2[i] == "G":
            if str2[i+1] == "G":
                v.append(i)
    return v

print(indicaIndexGlicina(str2))

print(str[:100])
def retorna100Primeiros(str):
    retorno = ""
    i = 0
    while i < 100:
        retorno += str[i]
        i += 1
    return retorno

print(retorna100Primeiros(str))

# substitui em todas as ocorrências
print(str.replace("SSSR", "AAAA"))
print(str.split("SSSR"))
