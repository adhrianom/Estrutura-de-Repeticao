n_bandeja = int(input())

quebrou = 0
n_quebrou = 0

for _ in range(n_bandeja):
    n_latas, n_copos = (int(x) for x in input().split())
    if n_latas > n_copos:
        quebrou += n_copos
    else:
        n_quebrou += 1

print(f"{quebrou}")