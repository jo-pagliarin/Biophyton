import math

# EXERCÍCIO 1
# CÁLCULO RMSD: desvio quadrático médio das posições atômicas com MATRIZ 
      
# DADOS GLICINA 1
            # NITROGÊNIO                  # CÁLCIO                      # CARBONO                  # OXIGÊNIO
first =[[108.304, 100.827, 67.992], [108.477, 100.389, 69.362], [109.907, 100.555, 69.817], [110.821, 100.799, 69.027]]

# DADOS GLICINA 2
            # NITROGÊNIO                  # CÁLCIO                      # CARBONO                  # OXIGÊNIO
second =[[107.670, 101.359, 70.074], [108.477, 100.389, 69.362], [109.513, 101.011, 68.450], [110.667, 100.572, 68.425]]

tmp_nitrogenio = pow((first[0][0] - second[0][0]), 2) + pow((first[0][1] - second[0][1]), 2) + pow((first[0][2] - second[0][2]), 2)
tmp_calcio = pow((first[1][0] - second[1][0]), 2) + pow((first[1][1] - second[1][1]), 2) + pow((first[1][2] - second[1][2]), 2)
tmp_carbono =  pow((first[2][0] - second[2][0]), 2) + pow((first[2][1] - second[2][1]), 2) + pow((first[2][2] - second[2][2]), 2)
tmp_oxigenio =  pow((first[3][0] - second[3][0]), 2) + pow((first[3][1] - second[3][1]), 2) + pow((first[3][2] - second[3][2]), 2)
soma = tmp_nitrogenio + tmp_calcio + tmp_carbono + tmp_oxigenio
rmsd = math.sqrt(soma/len(first))
print(round(rmsd, 2))


# EXERCÍCIO 2 - Calculando percentual GC
seq_A = "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
seq_B = "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"

count_g = 0
count_c = 0
for base in seq_A:
    if base == "G":
        count_g += 1
    elif base == "C": 
        count_c += 1
        
for base in seq_B:
    if base == "G":
        count_g += 1
    elif base == "C": 
        count_c += 1
        

perc = count_g/count_c
print(round(perc, 2))

