# 5. Registro de Alunos
# Descrição: Crie uma classe Aluno com atributos para nome,
# matrícula e curso. Adicione métodos para mudar o curso do
# aluno e outro para exibir as informações do aluno.

class Aluno:
    def __init__ (self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def set_curso(self, curso):
        self.curso = curso


    def exibir (self):
        print(f'{self.nome}\n{self.matricula}\n{self.curso}')
        print(20*"_")

def main():
    aluno1 = Aluno('Sidinei','1001','ADS')         
    aluno2 = Aluno('Renoir','1000','BD') 
    aluno1.exibir()
    aluno2.exibir()
    aluno1.set_curso("BD")
    aluno1.exibir()
    aluno2.exibir()

if __name__=='__main__':
    main()