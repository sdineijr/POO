# Exercício 1: Básico de Membros Públicos e Privados

# Crie uma classe ContaBancaria que tenha um atributo
# privado saldo e um atributo público titular. Inicialize ambos
# os atributos no método __init__. Em seguida, crie um método
# para depositar dinheiro e outro para exibir o saldo, garantindo
# que o saldo não possa ser acessado diretamente de fora da
# classe.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular
    
    
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito Concluido")
            print(40*"_")
        else:
            print("Depósito Negado")
            print(40*"_")
    
    def exibir(self):
        print(f'Saldo de {self.titular} é: {self.__saldo}')
        print(40*"_")

def main():
    sidinei = ContaBancaria(100.00, "Sidinei")
    sidinei.exibir ()
    sidinei.deposito (150.75)
    sidinei.exibir ()
    sidinei.deposito (-10)
    sidinei.exibir ()


if __name__ == "__main__":
    main()