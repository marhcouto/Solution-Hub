# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))

print(len(A.union(B)))