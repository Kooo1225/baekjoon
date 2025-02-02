import sys
input = sys.stdin.readline

m, n = map(int, input().split())
numbers = [[0] * (m + 1)]
prefix = [[0] * (m + 1) for _ in range(m+1)]

for i in range(m):
    row = [0] + [int(x) for x in input().split()]
    numbers.append(row)

for i in range(m + 1):
    for j in range(1, m + 1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + numbers[i][j]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x1 -1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

    print(result)
