from datetime import datetime


class Pessoa:
    ano_atual = datetime.strftime(datetime.now(), '%Y')
    
    #métodos de instância 
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        if self.comendo: #não precisa do True
            print(f'{self.nome} já está comendo')
            return #cessa o código
            
        #else...
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
    def get_ano_atual(ano_atual):
        return ano_atual
        
    def get_ano_nasc(self, ano_atual):
        return (ano_atual - self.idade)
    
    #métodos de classe
    def por_ano_nasc(cls, nome, ano_nascimento):

        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    
    