def primo (x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


number = int(input('Numero: '))
primo(number)

if primo(number):
    print(number, 'é primo')
else:
    print(number, 'Não é primo')