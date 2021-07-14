if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    maximum = max(arr)
    runnerUp = -1000000
    
    for element in arr:
        if runnerUp < element and element < maximum:
            runnerUp = element
            
    print(runnerUp)
