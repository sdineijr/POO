# Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
# - Solicite os dados do usuário
# - Utilize o ra do aluno como chave e uma lista de três notas como valor.
# - Percorra o dicionário e exiba a média de cada aluno.
# Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]}

alunos = {}

for _ in range(5):
    ra = input("Digite o RA do aluno: ")
    notas = []
    
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i} do aluno com RA {ra}: "))
        notas.append(nota)
    
    alunos[ra] = notas

print("\nMédia das notas de cada aluno:")
for ra, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"RA: {ra}, Média: {media:.2f}")