# seq1 = "ATATATAT"
# seq2 = "TATATATA"
# seq1 = "ACTGACTG"
# seq2 = "TCAGCCTG"
# seq1 = "ACTGACTG"
# seq2 = "GCCTG"
seq1 = "ATAGATAT"
seq2 = "TACATATA"

if len(list(seq1)) > len(list(seq2)):
    tamMaior = len(list(seq1))
    tamMenor = len(list(seq2))
else:
    tamMaior = len(list(seq2))
    tamMenor = len(list(seq1))

erros = 0
for i in range(tamMenor):
    if list(seq1)[i] != list(seq2)[i]:
        erros += 1
contador = tamMaior - tamMenor
erros += contador   

print(f'A distância de Hamming entre as sequências {seq1} e {seq2} é {erros}')

