# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
list1 = input().split()
input()
list2 = input().split()
sym = [int(x) for x in list(set(list1).symmetric_difference(set(list2)))]
sym.sort()
for i in sym:
    print(i)