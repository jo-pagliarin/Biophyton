def maximo(c1, c2, cima, lado, diagonal):
    if (c1 == c2 and (diagonal+1) >= cima and (diagonal+1) >= lado):
        diagonal = diagonal + 1
        return diagonal
    elif (lado >= cima and lado >= diagonal):
        return lado
    else:
        return cima
    
def ponteiro(c1, c2, cima, lado, diagonal):
    if (c1 == c2 and (diagonal+1) >= cima and (diagonal+1) >= lado):
        diagonal = diagonal + 1
        return '\\'
    elif (lado >= cima and lado >= diagonal):
        return '_'
    else:
        return '|'
    
def imprimeMatriz(v, w, pontuacao, ponteiros):
    print('\t', end='')
    for j in range(0, len(v)):
        print(v[j], end='\t')
    print()
    for i in range(0, len(w)):
        print(w[i], end='\t')
        for j in range(0, len(v)):
            print(pontuacao[i][j], ponteiros[i][j], end='\t', sep='')
        print()
    print()
    
def geraAlinhamento(v, w, pontuacao, ponteiros):
    # o alinhamento é gerado de trás para frente
    ali_v = ''
    ali_w = ''
    i = len(w) - 1
    j = len(v) - 1
    while ((i != 0) or (j !=0)):
                if (ponteiros[i][j] == '\\'):
                    ali_v = v[j] + ali_v
                    ali_w = w[i] + ali_w
                    j-=1
                    i-=1
                elif (ponteiros[i][j] == '_'):
                    ali_v = v[j] + ali_v
                    ali_w = '_' + ali_w
                    j-=1
                else:
                    ali_v = '_' + ali_v
                    ali_w = w[i] + ali_w
                    i-=1
    print(f'Distância de Needleman: {pontuacao[len(w)-1][len(v)-1]}')
    print(ali_v)
    print(ali_w)
                    

 # longest common subsequence (maior subsequência comum)
def lcs(v, w):
    # colunas (lineares)
    pontuacao = [0]*len(v)
    ponteiros = ['']*len(v)
    
    # linhas (não lineares, mas, sim, subsequentes)
    for i in range(len(w)):
        pontuacao[i] = [0]*len(v)
        ponteiros[i] = ['']*len(v)
    
    # todas as linhas da coluna zero são zeradas e apontam para cima
    for i in range(len(w)):
        ponteiros[i][0] = '|'
        
    # todas as colunas da linha zero são zeradas e apontam para a direita
    for j in range(len(v)):
        ponteiros[0][j] = '_'
            
    # algoritmo para preenchimento da matriz
    for i in range(1, len(w)):
        for j in range(1, len(v)):
            pontuacao[i][j] = maximo(w[i], v[j], pontuacao[i-1][j], pontuacao[i][j-1], pontuacao[i-1][j-1])
            ponteiros[i][j] = ponteiro(w[i], v[j], pontuacao[i-1][j], pontuacao[i][j-1], pontuacao[i-1][j-1])
            
    imprimeMatriz(v, w, pontuacao, ponteiros)
    geraAlinhamento(v, w, pontuacao, ponteiros)


# PROGRAMA PRINCIPAL
# Coloca-se o primeiro caracter como inválido, a fim de zerar a primeira posição. Isso é útil: 
# 1) pois a primeira linha e a primeira coluna da Tabela de Needleman-Wunsh são zeradas; 
# 2) para deixar o índice das sequências em conformidade com o tamanho da sequências. 
v = ['*', 'A', 'T', 'C', 'G', 'T', 'A', 'C'] 
w = ['*', 'A', 'T', 'G', 'T', 'T', 'A', 'T'] 
lcs(v,w)


