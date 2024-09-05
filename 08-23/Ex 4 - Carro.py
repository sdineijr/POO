# 4. Veículo
# Descrição: Implemente uma classe Carro com atributos para
# marca, modelo, ano e quilometragem. Inclua métodos para
# dirigir o carro, que aumenta a quilometragem, e outro método
# para exibir informações do carro.

class Carro:
    def __init__ (self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def set_quilometragem(self, quilometragem):
        self.quilometragem += quilometragem

    def exibir (self):
        print(f'{self.marca}\n{self.modelo}\n{self.ano}\n{self.quilometragem:,.2f}')
        print(20*"_")

def main():
    car1 = Carro('Renault','Logan','2010',10000)         
    car2 = Carro('Fiat','Uno','2012',5000) 
    car1.exibir()
    car2.exibir()
    car1.set_quilometragem(5000)
    car1.exibir()
    car2.exibir()

if __name__=='__main__':
    main()