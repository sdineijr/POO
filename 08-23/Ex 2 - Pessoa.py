class Pessoa:
    def __init__ (self, nome, idade, endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço

    def set_endereço(self, endereço):
        self.endereço = endereço
    
    def exibir(self):
        print(self.nome)
        print(self.idade)
        print(self.endereço)
