import numpy as np 

A = "agtcatc"
B = "ucaguag"

A = A.upper()
B = B.upper()

seqA = []
seqA = list(A)
seqB = []
seqB = list(B)

# print(f'Sequência A: {seqA}')
# print(f'Sequência b: {seqB}')

def constroiSequencia():
    sequencia = []
    for i in range(2):
        linha = []
        for j in range(len(seqA)):
            if (i == 0):
                list.append(linha, seqA[j])
            else:
                list.append(linha, seqB[j])
        sequencia = sequencia + [linha]
    return sequencia

aux = []
aux = constroiSequencia()
for c in range(2): 
   print(f'{aux[c]}\n')
   
print(np.matrix(aux))
