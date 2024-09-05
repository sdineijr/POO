nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

print("01) Quais são os clientes de cada uma, separadamente.")
for i in range(6):
    print(f'nubank:{nubank}, C6:{c6}, Inter:{inter}')


print('__________________')
print ("02) Quais são os clientes de todas as concorrentes.")
for clientes in nubank | c6 | inter:
    print(f'{clientes}', end=', ')

print()
print('________________________________________________________________')

print ("03) Quais são os clientes da Nubank que também são clientes do C6.")
for clientes in nubank & c6:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print ("04) Quais são os clientes da Nubank que também são clientes do Inter.")
for clientes in nubank & inter:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print ("05) Quais são os clientes do C6 que também são clientes do Inter.")
for clientes in inter & c6:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print ("06) Quais são os clientes apenas da Nubank.")
exclusivos_nubank = nubank - (c6 | inter)

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print("07) Quais são os clientes apenas do C6.")
exclusivos_nubank = c6 - (nubank | inter)

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print ("08) Quais são os clientes apenas do Inter.")
exclusivos_nubank = nubank ^ c6

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print ("09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.")
exclusivos_nubank = nubank ^ c6

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print("10 Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.")
exclusivos_nubank = nubank ^ inter

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print("11 Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.")
exclusivos_nubank = c6 ^ inter

for clientes in exclusivos_nubank:
    print(f'{clientes}')

print()
print('________________________________________________________________')

print("Quais são os clientes das três simultaneamente.")
for clientes in nubank & c6 & inter:
    print(f'{clientes}')

print()
print('________________________________________________________________')