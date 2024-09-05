# Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário.
# - Solicite os dados ao usuário
# - Utilize o nome do produto como chave e o preço como valor.
# - Percorra o dicionário e exiba o nome dos produtos com preço
# superior a R$ 50,00.
# Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {caneta: 3.0, Pen drive: 100.0,Teclado: 30.0, Lápis: 1.5}

produtos = {}

for i in range (5):
    nome = input('Produto: ')
    valor = float(input('Valor: '))
    produtos[nome] = valor


for nome, valor in produtos.items():
    if valor > 50.00:
        print(f"{nome}: R$ {valor:.2f}")