class Livro:
    def __init__ (self, titulo, autor, ano_de_publicaçao, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicaçao = ano_de_publicaçao
        self.disponibilidade = disponibilidade

    def emprestar(self):
        if self.disponibilidade == "indisponivel":
            print(f'{self.titulo} está indisponivel')
            print(10*"_")
        else:
            self.disponibilidade = "indisponivel"
            print(f'{self.titulo} Já esta disponivel na biblioteca')
            print(10*"_")

    def devolver(self):
        self.disponibilidade = "disponivel"

    def imprimir(self):
        print(self.titulo)
        print(self.autor)
        print(self.ano_de_publicaçao)
        print(self.disponibilidade)
        print(10*"_")

def main():
    livro1 = Livro("A Culpa é das Estrelas", "John Green" , "2014", "disponivel")
    livro1.imprimir()
    livro1.emprestar()
    livro1.imprimir()
    livro1.devolver()
    livro1.imprimir()

if __name__ == "__main__":
    main()

