def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(0, len(string)):
        if string[i].lower() in "aeiou":
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin {0}".format(kevin))
    elif stuart > kevin:
        print("Stuart {0}".format(stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)