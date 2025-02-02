import sys
input = sys.stdin.readline

m, n = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_numbers = [0]
temp = 0
for i in numbers:
    temp += i
    prefix_numbers.append(temp)

for i in range(n):
    i, j = map(int, input().split())
    print(prefix_numbers[j] - prefix_numbers[i - 1])
