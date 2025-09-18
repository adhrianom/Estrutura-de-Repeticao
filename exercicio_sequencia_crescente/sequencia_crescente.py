sequencia = []
while True:
    x = int(input())
    if x == 0:
        break
    linha = ""
    for i in range(1, x + 1):
        if i == x:
            linha += str(i)
        else:
            linha += str(i) + " "
    sequencia.append(linha)

print('\n'.join(sequencia))

