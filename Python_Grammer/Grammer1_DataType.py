#정수형
a = 777
print(a)

a = -5
print(a)

a = a + 5
print(a)

#실수형
a = 5.
print(a)

a = -.5
print(a)

#지수형
#지수는 실수형
#정수형을 원할경우 int 붙이기
a = 1e9
print(a)

a = 53.25e1
print(a)

a = 4324e-4
print(a)

#실수형의 오차
a = 0.3 + 0.6
print(a)  # 0.899999999

if a == 0.9:
    print(True)
else:
    print(False)  # False

#실수형 오차 해결, round()함수 : 반올림
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)  # True

#연산
# 나누기 연산(/)의 자료형은 실수형이다.
# 몫을 얻기 위한 몫 연산자 = //
# 거듭 제곱 연산자 = **
a = 7
b = 3

#나누기
print(a / b)
#나머지
print(a % b)
#몫
print(a // b)
#거듭제곱
print(a**b)
#제곱근
print(a**0.5)


