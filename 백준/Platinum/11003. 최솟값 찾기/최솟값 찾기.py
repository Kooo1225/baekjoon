from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
checkList = list(map(int, input().split()))
myList = deque()

for i in range(N):
    while myList and myList[-1][0] > checkList[i]:
        myList.pop()
    myList.append((checkList[i], i))
    if myList[0][1] <= i - L:
        myList.popleft()
    print(myList[0][0], end= " ")