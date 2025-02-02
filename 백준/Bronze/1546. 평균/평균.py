import sys

test_cnt = int(input())
test_score = list(map(int, sys.stdin.readline().split()))
max_score = max(test_score)

for i in range(test_cnt):
    test_score[i] = test_score[i] / max_score * 100

print(sum(test_score) / test_cnt)

