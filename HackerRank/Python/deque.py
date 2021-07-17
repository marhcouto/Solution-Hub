from collections import deque
d = deque()

n = int(input())

for i in range(n):
    line = input().split()
    getattr(d, line[0])(*[line[1]] if len(line) > 1 else [])
    
for i in d:
    print(i, end = " ")
