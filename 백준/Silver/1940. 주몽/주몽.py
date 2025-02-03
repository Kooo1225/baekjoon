import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = sorted(list(map(int, input().split())))

count, start, end = 0, 0, n - 1
while start < end:
    if numbers[start] + numbers[end] < m:
        start += 1
    elif numbers[start] + numbers[end] > m:
        end -= 1
    else:
        count += 1
        end -= 1
        start += 1

print(count)