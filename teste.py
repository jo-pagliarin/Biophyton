seq1 = "sdt"  # horizontal COLUNAS
seq2 = "tczxczzxr"  # vertical LINHAS 
seq1 = list(seq1)
seq2 = list(seq2)


def criaMatriz():
    matriz = [] 
    matriz *= len(seq1)+1 
    for linha in range(len(seq1)+1): 
        matriz.append([1]*int(len(seq2)+1))
    criaCabecalho(matriz)

def formataMatriz(matriz):
    for linha in range(len(seq1)+1): 
        for coluna in range(len(seq2)+1):
            print(f'{matriz[linha][coluna]}', end= ' ') 
        print() 

def criaCabecalho(matriz):
    matriz[0][0] = 0
    for linha in range(1,len(seq1)+1): 
        matriz[linha][0] = seq1[linha-1]
    for coluna in range(1, len(seq2)+1):
        matriz[0][coluna] = seq2[coluna-1]
    formataMatriz(matriz)
    
matriz = criaMatriz()

