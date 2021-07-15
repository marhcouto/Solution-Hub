input()
list1 = input().split()
input()
list2 = input().split()

print(len(set(list1).symmetric_difference(set(list2))))