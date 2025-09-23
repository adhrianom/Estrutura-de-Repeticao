num = int(input())
binario = ""

if num == 0:
    print(0)
else:
    while num > 0:
        binario += str(num % 2)
        num //= 2
    print(binario[::-1])