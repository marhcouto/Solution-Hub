def average(array):
    # your code goes here
    heightSet = set(array)
    hSum = 0
    for h in heightSet:
        hSum += h
    return hSum  / len(heightSet)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)