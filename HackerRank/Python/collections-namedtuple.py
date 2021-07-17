# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
fields = input().split()
Student = namedtuple('Student',fields)

total = 0
for i in range(N):
    field1, field2, field3, field4 = input().split()
    student = Student(field1, field2, field3, field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))