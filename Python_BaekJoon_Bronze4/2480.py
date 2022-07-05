a = list(map(int,input().split()))
num = 0
b = 0
if a[0] == a[1] == a[2]:
    num = 10000 + (a[0]*1000)
if a[0] != a[1] != a[2]:
    for i in range(0,3):
        if a[i] > b:
            b = a[i]
        num = b * 100
if a[0] == a[1] and a[0] != a[2]:
    num = 1000 + (a[0]*100)
if a[0] == a[2] and a[1] != a[2]:
    num = 1000 + (a[0]*100)
if a[1] == a[2] and a[0] != a[2]:
    num = 1000 + (a[1]*100)
print(num)