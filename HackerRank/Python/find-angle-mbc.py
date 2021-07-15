# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = float(input())
BC = float(input())
degree_sign= u'\N{DEGREE SIGN}'

print(str(int(round(math.degrees(math.atan2(AB,BC))))) + degree_sign)
