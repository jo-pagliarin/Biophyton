class Aluno:
    def __init__(self, nome, nota1, nota2, situacao):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.situacao = ["aprovado", "reprovado", "em recuperação"]


n = 3

alunos = []

def leAluno(n):
    i = 0
    while (i < n):
        aux = Aluno(input("Nome do aluno: "), input("Nota 1: "),
                    input("Nota 2: "), input("Situação: "))
        alunos.append(aux)
        i += 1

leAluno(n)
