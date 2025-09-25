num = int(input())

eh_regular = False

while num != 1:
    if num % 2 == 0:
        num //= 2
    elif num % 3 == 0:
        num //= 3
    elif num % 5 == 0:
        num //= 5
    else:
        eh_regular = False
        break
    eh_regular = True
    
print(eh_regular)
