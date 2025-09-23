import math

p = 1

while math.factorial(p) <= p**10:
    p += 1

print(p)