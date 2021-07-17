from collections import defaultdict

d = defaultdict(list)
temp = list(map(int, input().split()))
n, m = temp[0], temp[1]

for i in range(n):
    d[input()].append(i)
    
for i in range(m):
    letter = input()
    if len(d[letter]) == 0:
        print(-1)
        continue
    for pos in d[letter]:
        print(pos + 1, end=" ")
    print()
    