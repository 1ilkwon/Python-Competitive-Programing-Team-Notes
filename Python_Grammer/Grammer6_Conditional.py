"""
조건문
프로그램의 흐름을 제어하는 문법
조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있다.

기본적인 형태 : if ~ elif ~ else
조건문에 따라 elif나 else를 사용하지 않아도 된다.
"""
x = 15
if x >= 10:
    print("x >= 10")
if x >= 0 :
    print("x >= 0")
if x >= 30:
    print("x >= 30")

"""
들여쓰기
파이썬에서는 코드의 블록을 들여쓰기로 지정
탭을 사용하는 쪽과 공백 문자를 여러 번 사용하는 쪽으로 두 진영이 있습니다.
 - 이 논쟁은 아직 활발함
파이썬 스타일 가이드라이에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정하고 있다.
"""
a = -5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 > a")

# 성적 구간에 따른 예시
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('F')

"""
비교 연산자 
특정한 두 값을 비교할 때 이용
1. X == Y : X와 Y가 서로 같을 때 TURE
2. X != Y : X와 Y가 서로 다를 때 TURE
3. X > Y : X가 Y보다 클 때 TRUE
4. X < Y : X가 Y보다 작을 때 TRUE
5. X >= y : X가 Y보다 크거나 같을 때 TRUE
6. X <= y : X가 Y보다 작거나 같을 때 TRUE 
"""
"""
논리 연산자
논리 값 사이의 연산을 수행할 때 사용
1. X and Y : X와 Y가 모두 TRUE일 때 TRUE
2. X or Y : X와 Y 중에 하나만 True이면 TRUE
3. not X : X가 FALSE일 때 TRUE
"""
if True or False:
    print('yes')
else:
    print('False')

a = 15

if a <= 20 and a >= 0:
    print('Yes')

"""
기타 연산자 
다수의 데이터를 담는 자료형을 위해 in연산자와 not in 연산자가 제공
 - 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능하다.

1. x in 리스트 : 리스트 안에 x가 들어가 있을 때 TRUE
2. x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 TRUE
"""