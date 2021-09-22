import numpy

def arrays(arr):
    l = list(map(float, arr))
    l.reverse()
    return numpy.array(l, dtype = float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)