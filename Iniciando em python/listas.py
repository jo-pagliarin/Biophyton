import numpy
bases_nitrogenadas = ("A", "T", "C", "G", "U")
# tupla: imutável =+6> nada pode ser alterado. Sempre usa parentêses

seq1DNA = "agtcatc"
seq1RNA = "ucaguag"
seq2DNA = "actgatt"
seq2RNA = "ugacuaa"

sequenciaDNA = []
sequenciaRNA = []
sequenciaDNA = seq2DNA + seq1DNA
sequenciaRNA = seq2RNA + seq1RNA

print(sequenciaDNA)
print(sequenciaRNA)








# def converteMinuscula(seq1DNA, seq1RNA):
#     seq1DNA = seq1DNA.upper()
#     seq1RNA = seq1RNA.upper()
#     return [seq1DNA, seq1RNA]

# resultado = converteMinuscula(seq1DNA, seq1RNA)
# print(resultado)
# seq1DNA = resultado[0]
# seq1RNA = resultado[1]
# print(seq1DNA)
# print(seq1RNA)

# def converteStringRNA(seq1RNA):
#     seq1RNA = seq1RNA.upper()
#     return (seq1RNA)

# seq1RNA = converteStringRNA(seq1RNA)

# print(f'Sequencia DNA: {seq1DNA}')
# print(f'Sequencia RNA: {seq1RNA}')

# def constroiMatriz():
#     matriz = []
#     for i in range(2):
#         linha = []
#         for j in range(len(seq1DNA)):
#             list.append(linha, "x")
#         matriz = matriz + [linha]
#     return matriz

# # print('{:2}'.format(constroiMatriz()))