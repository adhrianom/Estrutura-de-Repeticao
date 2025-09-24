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
            
n, m = [int(x) for x in input().split()]

p1 = n
p2 = m

while not eh_primo(p1):
    p1 -= 1

while not eh_primo(p2):
    p2 += 1

produto = p1 * p2
print(produto)