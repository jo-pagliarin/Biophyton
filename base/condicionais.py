# # EXERCÍCIO 1
sequencia = ''
sequencia = list(sequencia)


def validaSeq(sequencia):
    if (len(sequencia) < 50):
        print("A sequência não é válida")
    else:
        print("A sequência é válida")


validaSeq(sequencia)

# EXERCÍCIO 3
def definePeptideo(peptideo):
    if (len(peptideo) == 2):
        print("É um dipeptideo")

    elif (len(peptideo) == 3):
        print("É um tripeptideo")

    else:
        print("É um polipeptideo")


# EXERCÍCIO 2
peptideo = 'aaaaaaaaaaa'
peptideo = list(peptideo)

def validaPeptidio(peptideo):
    if (len(peptideo) < 2 or len(peptideo) > 50):
        print("O peptideo não é válido")
    else:
        print("O peptideo é válido")
        definePeptideo(peptideo)

validaPeptidio(peptideo)

# EXERCÍCIO 4 com DICIONÁRIO
aminoac = "L"
amoniac = list(aminoac)
descricao = []

vetores = {
    'hidrofobico': ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K'],
    'pequeno': ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V'],
    'polar': ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E'],
    'carregado': ['D', 'E', 'R', 'K', 'H'],
    'aromatico': ['F', 'Y', 'W', 'H'],
    'minusculo': ['A', 'C', 'G', 'S'],
    'alifatico': ['I', 'L', 'V'],
    'hidroxila': ['T', 'S'],
    'acido': ['N', 'Q'],
    'enxofre': ['C', 'M']
}


def descreveAminoac(vetores):
    for caracteristica in vetores:
        for base in vetores[caracteristica]:
            if base == aminoac:
                print(caracteristica)

descreveAminoac(vetores)

# EXERCÍCIO 5 
def verificaPolaridade(vetores):
    vetor = list(vetores['polar'])
    for base in vetor:
        if base == aminoac:
            print(f'{aminoac} é polar')
            return
    print(f'{aminoac} tem carga neutra')

verificaPolaridade(vetores)

