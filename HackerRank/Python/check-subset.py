# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    _, A = input(), set(map(int, input().split()))
    _, B = input(), set(map(int, input().split()))
    print(A.issubset(B))