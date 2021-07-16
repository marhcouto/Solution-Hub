# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happy = 0
for num in arr:
    if num in A:
        happy += 1
    if num in B:
        happy -= 1
        
print(happy)