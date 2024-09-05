class Produtos:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def adicionar(self, quantidade):
        self.quantidade += quantidade
    
    def remover(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print('Vai da não')

    def exibir(self):
        print(self.nome)
        print(self.preço)
        print(self.quantidade)