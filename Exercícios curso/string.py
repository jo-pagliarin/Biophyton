# EX 01
sequencia = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

# LETRA A
A = print(f'Tam = ', len(sequencia))
tam = len(sequencia)
B = print(tam)
print(A == B)

# LETRA B
x = sequencia.count("LL")
print(x)
# em python, string não é entendida como um vetor 

# index() retorna a primeira ocorrência 
# em seq = AALLL, para "LL", retorna 2

## LETRA B COM FUNÇÃO
def contaLeucina():
    count = 0
    for i in range(len(sequencia) - 1):
        if sequencia[i] == "L":
            if sequencia[i + 1] == "L":
                count += 1
    return count

print(contaLeucina())

# LETRA C
print(f'Posição GG: ', sequencia.rfind("GG"))
print(f'Posição RR: ', sequencia.rfind("RR"))
    
# LETRA D
print(sequencia[:100])

# LETRA E
sequencia = sequencia.replace('SSSR', 'ALA')
print(sequencia)

# LETRA D
sequencia = sequencia.split("ALA")
print(sequencia)

# EX 02
string = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."

# LETRA A
string = string.upper()
print(string)

# LETRA B
string = string.lower()
print(string)

# LETRA C 
string = string.title()
print(string)

# LETRA D
string = string.swapcase() 
print(string)

# EX 03 
# LETRA A
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"
print(len(insulin_signal))

#LETRA B
# retornando lista
print(insulin_signal.split("LLALLALWG"))

# LETRA C
# removendo virgula, transformando em string
print(''.join(insulin_signal.split("LLALLALWG")))

# LETRA D 
string = insulin_signal.replace("DPAAA", "LLALL")
print(string)

# EX 04
dna = 'GATGGAACTTGACGTAAACCTATATT'
rna = ''

def criaRNA(dna, rna):
    for i in range(len(dna)):
        if dna[i] == 'G':
            rna = rna + ''.ljust(1, 'C')
        elif dna[i] == 'C':
            rna = rna + ''.ljust(1, 'G')
        elif dna[i] == 'A':
            rna = rna + ''.ljust(1, 'U')
        else:
            rna = rna + ''.ljust(1, 'A')
    return(rna) 

rna = criaRNA(dna, rna)
print(dna)
print(rna)
print(len(dna) == len(rna))
print(type(rna))
      
# exemplo de função com número indefinido de parâmetros  
strTeste = ["amor" , "laranja" , "banana", "garrafa"]
def buscaPalavra(*palavras):
    for palavra in palavras:
        num =  strTeste.index(palavra)
        try:
            float(num)
            print(f'Achei a palavra na posição {num} do vetor, portanto, elemento número {num+1}')
        except ValueError:
            return
            
buscaPalavra("uva", "laranja", "garrafa")  



