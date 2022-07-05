import sys

a = list()
vowel='aeiou'
num = 0
while True:
    b = sys.stdin.readline().lower()
    if b.find("#")!=-1:
        break
    for i in vowel:
        num += b.count(i)
    a.append(num)
    num = 0
for i in a:
    print(i)

# find() : 문자를 찾는 함수, 문자가 있으면 -1을 출력한다.
# for i in 변수 or 리스트 : 특정한 변수를 이용하여 'in'뒤에 오는 데이터에 포함되어 있는 원소를
# 첫번째 인덱스부터 차례대로 하나씩 방문한다.