import sys
input = sys.stdin.readline

n = int(input())
sum, count = 1, 1
start, end = 1, 1

while end != n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)