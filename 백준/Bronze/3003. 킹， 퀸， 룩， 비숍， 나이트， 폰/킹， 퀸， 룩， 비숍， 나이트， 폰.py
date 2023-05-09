chess = [1, 1, 2, 2, 2, 8]
tmp = list(map(int, input().split()))

for i in range(6):
    print(f'{chess[i] - tmp[i]}', end=' ')


