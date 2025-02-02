numbers = []
count = int(input())

for i in range(0, count):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)