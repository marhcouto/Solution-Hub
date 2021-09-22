import numpy

N, M, P = map(int, input().split())


list1 = []
list2 = []
for i in range(0, N):
    list1.append(list(map(int, input().split())))
for i in range(0, M):
    list2.append(list(map(int, input().split())))
    
print(numpy.concatenate((numpy.array(list1), numpy.array(list2))))
    
    
    