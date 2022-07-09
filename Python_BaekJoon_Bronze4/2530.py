A, B, C = map(int, input().split())
s = int(input())

a = A*3600
b = B*60
total = a + b + C + s

A = total // 3600
B = (total - A*3600) // 60
C = total - (A*3600) - (B*60)
a2 = (A // 24)
a1 = A - (a2*24)
if A > 23:
    print(a1, B, C, end='')
else:
    print(A, B, C, end='')
    

# 시 분 초를 이용하는 문제는 초단위로 환산하는 것을 생각해보기