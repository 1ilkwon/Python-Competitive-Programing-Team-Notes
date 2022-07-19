a = int(input())
b = int(input())
c = int(input())
d = int(input())
sec = a + b + c + d
min = sec //60
sec2 = sec - (60*min)
if 60 <= sec <= 3599:
    print(min)
    print(sec2)
