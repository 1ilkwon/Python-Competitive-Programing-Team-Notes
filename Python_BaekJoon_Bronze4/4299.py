c, d = map(int, input().split())
a = (c+d)/2
b = c - a
if a >= b and a % 1 != 0.5 and c >= d:
    print(int(a), int(b))
if b > a and a % 1 != 0.5 and c >= d:
    print(int(b), int(a))
if a < 0 or b < 0 or a % 1 == 0.5 or d > c:
    print(-1)
