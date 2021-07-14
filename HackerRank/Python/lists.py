if __name__ == '__main__':
    N = int(input())
    
    lista = []
    while N > 0:
        
        line = input() 
        line = line.split()
        
        if line[0] == "print":
            print(lista)
        elif line[0] == "append":
            lista.append(int(line[1]))
        elif line[0] == "remove":
            if int(line[1]) in lista:
                lista.remove(int(line[1]))
        elif line[0] == "insert":
            lista.insert(int(line[1]), int(line[2]))
        elif line[0] == "sort":
            lista.sort()
        elif line[0] == "pop":
            lista.pop()
        elif line[0] == "reverse":
            lista.reverse() 
        N -= 1
