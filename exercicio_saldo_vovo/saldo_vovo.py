num_dias, saldo = [int(x) for x in input().split()]

menor_saldo = saldo

for dia in range(num_dias):
    valor = int(input())
    saldo += valor
    if saldo < menor_saldo:
        menor_saldo = saldo

print(menor_saldo)
