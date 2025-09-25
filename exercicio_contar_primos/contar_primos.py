import math

def eh_primo(n: int):
        if n <= 1:
            return False
        elif n % 2 == 0 and n != 2:
            return False
        else:
            raiz = int(math.sqrt(n))
            for k in range(3, raiz + 1, 2):
                if n % k == 0:
                    return False
            return True

x = int(input())
y = int(input())

n_primos = 0

for _ in range(x, y + 1):
    if eh_primo(_):
        n_primos += 1
    

print(n_primos)