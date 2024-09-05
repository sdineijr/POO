number = int(input())
fatorial = number-1
total = 0

while True:
    if fatorial == 0:
        break
    total = number * fatorial
    fatorial -= 1
    number = total

print(total)

    


    