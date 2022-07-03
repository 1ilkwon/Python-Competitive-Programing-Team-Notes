year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)

# 논리 연산자에서 여러번에 조건을 부여할 경우 소괄호를 이용할 수 있다.