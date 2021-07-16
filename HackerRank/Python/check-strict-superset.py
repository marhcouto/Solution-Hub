# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
T = int(input())
res = True
for i in range(T):
    B = set(map(int, input().split()))
    res &= A.issuperset(B) and len(A) > len(B) 
print(res)