

# def constroiMatriz():
#     matriz = []
#     linha = len(string2) + 2 # 6 
#     coluna = len(string1) + 2 # 7 
#     for linha in range(linha):
#         matriz.append([calculaPontuacao(linha, j)]* (coluna))
#         if linha > 0: # linha começa em 1
#             matriz[linha][1] = linha - 1
#         if linha > 1: # linha começa em 2 
#             matriz[linha][0] = string2[linha - 2] 
#     matriz[0][0] = matriz[0][1] = matriz[1][0] = " "
#     matriz[0][2:] = list(string1)[0:]
#     matriz[1][1:] = range(0, len(string1) + 1)
#     for linha in range(0,  len(string2) + 2):
#         for coluna in range(0, len(string1) + 2):
#             print(f'{matriz[linha][coluna]}', end= '  ') 
#         print()
#         print()
        
# def calculaPontuacao(linha, coluna):
#     return(({linha}, {coluna}))  
    
# constroiMatriz()

string1 = "caixa" 
string2 = "cama"

for linha in range(len(string2)):
    for coluna in range(len(string1)):
        if string2[linha] == string1[coluna]:
             
        valor = f'{string2[linha]}{string1[coluna]}'
        print(valor, end= "  ")
    print()
