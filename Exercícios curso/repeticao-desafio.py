# EXERCÍCIO 1
def converteTemperatura():
    listTc = []
    for tf in range(1,151):
        tc = (tf - 32)*5/9
        listTc.append(round(tc,2))
    print(listTc)

# converteTemperatura()

# EXERCÍCIO 2
sequencias = ['ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT', 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN', 'AAAAAAGCCCCUAAGC', 'AAAAAAGCCCCTAAGC', 'GGGGAAAAAGCCCCUAAGC']
dna = ['A', 'G', 'T', 'C']
rna = ['A', 'G', 'U', 'C']
proteina = ['A', 'C', 'D', 'E', 'F', 'G','H','I','K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def defineSequencia():
    proteinas = []
    dnas = []
    rnas = []
    for sequencia in sequencias:
        for base in sequencia:
            if not base in dna:
                if not base in rna:
                    proteinas.append(sequencia)
                    break
        if not sequencia in proteinas:
            for base in sequencia:
                if not base in dna:
                    rnas.append(sequencia)
            if not sequencia in rnas:
                dnas.append(sequencia)     
    print(f'São proteínas as sequências: {proteinas}')
    print(f'São dnas as sequências: {dnas}')
    print(f'São rnas as sequências: {rnas}')
                
# defineSequencia()

# EXERCÍCIO 3 
seq = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
def converteSeq():
    rna = ''
    for base in seq:
        if base == 'T':
            rna = rna + 'A'
        elif base == 'A':
            rna = rna + 'U'
        elif base == 'G':
            rna = rna + 'C'            
        else:
            rna = rna + 'G'
    print(rna)    
    
# converteSeq()

# EXERCÍCIO 4 - Fatorial de um número
n = 5

def calculaFatorial():
    fatorial = 1
    for i in range (1, n+1):
        fatorial = fatorial * i 
    print(fatorial)

# calculaFatorial()

# EXERCÍCIO 5 
n = 3
def imprimeTabuada():
    for i in range (1,11):
        print(f'{n}*{i} = {i*n}')
        
# imprimeTabuada()

# EXERCÍCIO 6 
seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
massa = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

def calculaMM():
    mm = 0
    for base in seq:
        for chave in massa.keys():
            if base == chave:
                mm = mm + massa[chave]
    print(round(mm,2))

# calculaMM()

# EXERCÍCIO 7 
defensinas = {'3PSM': 'KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC',
              '3PSN': 'KTCSNLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC', 
              '2NY9': 'ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF',
              '2NY8': 'ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN',
              '2NZ3': 'ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN',
              '2E3G': 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN',
              '2E3F': 'ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR',
              '2E3E': 'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF',
                '2E3H': 'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF'}

# letra A
def imprimeMenorSeq():
    menorTam = 100
    menoresChaves = []
    menoresSequencias = []
    for sequencia in defensinas:
        if len(defensinas[sequencia]) < menorTam:
            menorTam = len(defensinas[sequencia])
    for sequencia in defensinas:
        if len(defensinas[sequencia]) == menorTam:
            menoresChaves.append(sequencia)
            menoresSequencias.append(defensinas[sequencia])
    print(f'Menores chaves: {menoresChaves}')
    print(f'Menor tamanho: {menorTam}')
    print(f'Menores sequências: {menoresSequencias}')

# imprimeMenorSeq()

# letra B
def imprimeMaiorSeq():
    maiorTam = 0
    maioresChaves = []
    maioresSequencias = []
    for sequencia in defensinas:
        if len(defensinas[sequencia]) > maiorTam:
            maiorTam = len(defensinas[sequencia])
    for sequencia in defensinas:
        if len(defensinas[sequencia]) == maiorTam:
            maioresChaves.append(sequencia)
            maioresSequencias.append(defensinas[sequencia])
    print(f'Maiores chaves: {maioresChaves}')
    print(f'Maior tamanho: {maiorTam}')
    print(f'Maiores sequências: {maioresSequencias}')

# imprimeMaiorSeq()

# letra C
def calculaMedia():
    soma = 0
    for sequencia in defensinas:
        soma = soma + len(defensinas[sequencia])
    print(f'A média do tamanho das sequências é {soma/len(defensinas)}')
    
# calculaMedia()

# letra D
import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

defensinasLista = list(defensinas)
def calculaMediana():
    tamAmostra = len(defensinas)
    if tamAmostra % 2 != 0: 
        indice = int(round_up(tamAmostra/2, 0))
        chave = defensinasLista[indice-1]
        mediana = len(defensinas[chave])
        return mediana
    else:
        indice1 = int(tamAmostra/2)
        indice2 = int((tamAmostra/2) + 1)
        chave1 = defensinasLista[indice1-1]
        chave2 = defensinasLista[indice2-1]
        mediana =  (len(defensinas[chave1]) + len(defensinas[chave2]))/2
        return mediana
    
    
# print(f'A mediana da amostra é {calculaMediana()}')


