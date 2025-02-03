import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_numbers = [0] * n
prefix_numbers[0] = numbers[0]
c = [0] * m
answer = 0
for i in range(1, n):
    prefix_numbers[i] = (prefix_numbers[i - 1] + numbers[i])

for i in range(n):
    remainder = prefix_numbers[i] % m
    if remainder == 0:
        answer += 1
    c[remainder] += 1

for i in range(m):
    if c[i] > 1:
        answer += (c[i] * (c[i] - 1 ) // 2)

print(answer)