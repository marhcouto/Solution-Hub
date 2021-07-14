from collections import Counter

input()
shoeDict = Counter(input().split())
n = int(input())
shopperDict = {}
for i in range(n):
    string = input().split()
    if string[0] in shopperDict.keys():
        shopperDict[string[0]].append(int(string[1]))
    else:
        shopperDict[string[0]] = [int(string[1])]
    
purse = 0

for size in shopperDict.keys():
    while shoeDict[size] > 0 and 0 != len(shopperDict[size]):
        purse += shopperDict[size][0]
        del shopperDict[size][0]
        shoeDict[size] -= 1
    
print(purse)
