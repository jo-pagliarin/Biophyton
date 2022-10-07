class aluno:
    def __init__(self, nome, nota1, nota2, situacao):
        self.nome = nome 
        self.nota1 = nota1
        self.nota2 = nota2
        self.situacao = ["aprovado", "reprovado", "em recuperação"]

n = 5

def leAluno(n):
    i = 0
    while(i<n):
        a  = aluno(input("Nome do aluno: "), input("Nota 1: "), input("Nota 2: "), input("Situação: "))
        aluno.append(a)
        i += 1 
    
leAluno(n)