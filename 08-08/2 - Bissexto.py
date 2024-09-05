ano = int(input())

if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'esse ano {ano} é bissextos')
else:
    print(f'esse ano {ano} não é bissextos')