from operator import itemgetter

if __name__ == '__main__':
    
    l = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append((name, score))
        
    maximum = min(l, key = itemgetter(1))
    
    secMax = 100000
    for element in l:
        if (element[1] < secMax and element[1] != maximum[1]):
            secMax = element[1];
            
    l.sort()
            
    for element in l:
        if (element[1] == secMax):
            print(element[0])