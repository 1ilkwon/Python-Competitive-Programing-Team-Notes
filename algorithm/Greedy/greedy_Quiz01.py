n = input()
data = list(map(int, input().split()))
data.sort()
result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# 막힌 곳 뻥~
# for i in data 부분에서 i에는 data 인덱스 0부터 끝까지 인덱스 안에 데이터 값을 넣어준다
# 즉 count를 비교할 때 data[i]가 아닌 i 를 비교해 주면 data에 인덱스 0부터 데이터를 비교 하기 시작한다.

# 두번째
# 문제에서 공포도보다 크거나 같은 값에 구성원을 지정해 줘야한다 때문에 == 이 아닌 >=으로 해석해야한다.
