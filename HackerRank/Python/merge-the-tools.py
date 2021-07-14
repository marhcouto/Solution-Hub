def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        lista = []
        for letter in string[i:i + k]:
            if letter not in lista:
                lista.append(letter)
        print(''.join(lista))
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)