if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    num = 0
    avg = 0
    for grade in student_marks[query_name]:
        avg += grade / len(student_marks[query_name])
        num += 1
    print("{:.2f}".format(avg))
