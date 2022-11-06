
# for x in sequencias:
#     if x == "T":
#         print(f'É uma molécula de DNA!')
#         break
#     elif x == "U":
#         print(f'É uma molécula de RNA!')
#         break

#  MATRIZ 4 LINHAS E 3 COLUNAS
def constroiMatriz1():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(3):
            list.append(linha, 1)
        matriz = matriz + [linha]
    return matriz

print(constroiMatriz1())