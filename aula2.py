# Métodos em instância de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# Classe - Molse (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode garar várias instâncias.
# Na classe o self é a própria instância.


class Carro:
    def __init__(self, nome = 'Não informado'):
        self.nome = nome #Hard coded
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('Celta')
print(celta.nome)
celta.acelerar()