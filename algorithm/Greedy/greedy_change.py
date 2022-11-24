N = 1260 # 거스름 돈
count = 0 # 동전의 개수

# 가지고 있는 코인
array = [500, 100, 50, 10]

for coin in array :
    # 제일 큰 동전부터 차례로 몫을 구하기
    count += N // coin
    N %= coin

print(count)