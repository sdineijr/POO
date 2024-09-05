# Exercício 2: Getters e Setters Simples

# Crie uma classe Lampada com um atributo privado estado
# (ligado/desligado). Implemente métodos getters e setters para o
# atributo estado. O setter deve aceitar apenas os valores
# "ligado" ou "desligado" e alterar o estado da lâmpada de
# acordo.

class Lampada:
    def __init__(self):
        self.__estado = "Desligado"

    def set_estado(self, estado):
        if (estado == "desligado" or estado == "ligado"):
            self.__estado = estado
        else:
            print("Error")

    def get_estado(self):
        print(f'{self.__estado}')


def main():
    estado = Lampada ()
    estado.get_estado()
    estado.set_estado("on")
    estado.set_estado("ligado")
    estado.get_estado()
    

if __name__ == "__main__":
    main()