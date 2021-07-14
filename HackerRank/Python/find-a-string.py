def knuth_morris_pratt(pattern, text):
    if len(pattern) == 0 or len(text) == 0 or len(text) < len(pattern):
        return 0
        
    count = 0
    deslList = [0] * (len(pattern))
    k = 0
    for i in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[i]:
            k = deslList[k - 1]
        if (pattern[k] == pattern[i]):
            k = k + 1
        deslList[i] = k
    
    k = 0
    for i in range(0, len(text)):
        while k > 0 and pattern[k] != text[i]:
            k = deslList[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k >= len(pattern):
            count += 1
            k = deslList[k - 1]

    return count


def count_substring(string, sub_string):
    return knuth_morris_pratt(sub_string, string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)