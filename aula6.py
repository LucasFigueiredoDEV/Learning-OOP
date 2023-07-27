# __dict__ e vars para atributos de instâncias

class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade):
        self.nome =  nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade



p1 = Pessoa('João', 35)