seq1 = "atcgtac" # horizontal - coluna
seq2 = "atgttat" # vertical - linha 
seq1 = list(seq1.upper())
seq2 = list(seq2.upper())

class Celula: 
    def __init__ (self, pontuacao: int, seta: str):
        self.pontuacao = pontuacao
        self.seta = seta
        
    def __str__(self):
        return f'{self.seta}{self.pontuacao}'

def constroiPares():
    for linha in range(len(seq2)):
        for coluna in range(len(seq1)):
            valor = f'{seq2[linha]}{ seq1[coluna]} '
            if seq2[linha] == seq1[coluna]:
                if linha == 0 or coluna == 0:
                    valor = Celula(seta = "↖ ", pontuacao = 1)
            elif seq2[0] == seq1[0]:
                if linha == 0:
                    valor = Celula(seta = "← ", pontuacao = 1)
                elif coluna == 0:
                    valor = Celula(seta = "↑ ", pontuacao = 1) 
            elif seq2[0] != seq1[0]:
                if seq2[0] == seq1[coluna]:
                    valor = Celula(seta = "← ", pontuacao = 1)
                elif seq2[linha] == seq1[0]:
                    valor = Celula(seta = "↑ ", pontuacao = 1)
            print(valor, end= "  ")
        print()
            
constroiPares()
print()

for linha in range(len(seq2)):
        for coluna in range(len(seq1)):
            valor = f'{seq2[linha]}{ seq1[coluna]}'
            print(valor, end= "  ")
        print()