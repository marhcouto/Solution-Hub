import numpy

N, M = map(int, input().split())

list1 = list()
for i in range(0, N):
    list1.append(list(map(int, input().split())))
    
arr = numpy.array(list1)
print(arr.transpose())
print(arr.flatten())