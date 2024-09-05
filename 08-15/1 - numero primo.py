# Exercício 1: Números Primos
# '''Crie um programa que encontre e imprima os 20 primeiros números primos.
# Um número é considerado primo se ele é maior que 1 e possui exatamente
# dois divisores: 1 e ele mesmo. Utilize um loop while para iterar até
# encontrar 20 números primos e um loop for para contar a quantidade de
# divisores de cada número.'''

def primo (x):
    if x == 1:
            return False
    for i in range(2, x):    
        if x % i == 0:
            return False
    
    return True

cont = 0
number = 1
while cont < 20:
    if primo(number):
        print(number, 'é primo')
        cont += 1
    
    number += 1