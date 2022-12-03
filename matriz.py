seq1 = "atcgtac" 
seq2 = "atgttat" 
seq1 = list(seq1.upper())
seq2 = list(seq2.upper())
        
def criaMatriz():
    matriz = [] 
    matriz *= len(seq1)+1 
    for linha in range(len(seq2)+1): 
        matriz.append(["↖ 1"]*int(len(seq1)+1))
    criaCabecalho(matriz)

def formataMatriz(matriz):
    for linha in range(len(seq2)+1): 
        for coluna in range(len(seq1)+1):
            print(f'{matriz[linha][coluna]}', end= '   ') 
        print()
        print()

def criaCabecalho(matriz):
    matriz[0][0] = "   "
    for linha in range(1,len(seq2)+1): 
        matriz[linha][0] = seq2[linha-1]
    for coluna in range(1, len(seq1)+1):
        matriz[0][coluna] = str(seq1[coluna-1]) + "  "
    formataMatriz(matriz)
    
matriz = criaMatriz()

