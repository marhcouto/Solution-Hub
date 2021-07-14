from itertools import permutations

def main():
    answer = input()
    string = answer.split()[0]
    size = int(answer.split()[1]) 
    list1 = [''.join(x) for x in permutations(string, size)]
    list1.sort()
    for element in list1:
        print(element)

    
if __name__ == "__main__":
    
    main()
    