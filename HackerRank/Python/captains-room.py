# Enter your code here. Read input from STDIN. Print output to STDOUT
_, rooms = input(), list(map(int, input().split()))

d = {}

for i in rooms:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.items():
    if i[1] == 1:
        print(i[0])
        break
