import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted(list(map(int, input().split())))

count = 0
for idx in range(n):
    find = numbers[idx]
    i, j = 0, n - 1
    while i < j:
        if numbers[i] + numbers[j] == find:
            if i != idx and j != idx:
                count += 1
                break
            elif i == idx:
                i += 1
            elif j == idx:
                j -= 1
        elif numbers[i] + numbers[j] < find:
            i += 1
        else:
            j -= 1

print(count)