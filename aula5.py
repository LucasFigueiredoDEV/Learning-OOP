# Atriutos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        ano_nascimento = Pessoa.ano_atual - self.idade
        return f'O ano de nascimento do {self.nome} é {ano_nascimento}'
    

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

