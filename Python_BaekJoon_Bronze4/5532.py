import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a = A / C
a = math.ceil(a)
b = B / D
b = math.ceil(b)
if a >= b:
    print(L-a)
if a < b:
    print(L-b)

# 올림 = math.ceil()
# 내림 = math.floor()
# 반올림 = round()