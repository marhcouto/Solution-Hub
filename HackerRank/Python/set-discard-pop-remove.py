n = int(input())
s = set(map(int, input().split()))

N = int(input())


for i in range(N):
    instruction = input().split()
    if instruction[0] == "pop":
        s.pop()
    elif instruction[0] == "remove":
        s.remove(int(instruction[1]))
    elif instruction[0] == "discard":
        s.discard(int(instruction[1]))

sum1 = 0
for i in s:
    sum1 += i
    
print(sum1)
