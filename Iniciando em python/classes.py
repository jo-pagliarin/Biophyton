class aluno:
    def __init__(self, nome, nota1, nota2, situacao):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.situacao = ["aprovado", "reprovado", "em recuperação"]
        if situacao in situacao:
            self.situacao = situacao
        else:
            raise Exception("Campo inválido")
        
aluno1 = aluno("lucas", 8, 9, "aprovado")
aluno2 = aluno("joao", 6, 5, "reprovado")
aluno3 = aluno("matheus", 4, 2, "não encontrado")

print(aluno1.situacao)
print(aluno3.situacao)

