# n과 k에 입력 값을 받기 위한 변수
n, k = map(int, input().split())

# 횟수를 저장할 변수
result = 0

# 몫과 나머지를 저장할 변수
share = 0
rest = 0

share = n // k
rest = n % k

# n이 k로 나눠질 경우
if share > 0:
    result = share + rest
    print(result)
# n이 k로 나눠지지 않을 경우
else:
    print(rest)

# ------------------------두번째 풀이--------------------------
# n1, k1에 입력 값을 받기 위한 변수
n1, k1 = map(int, input().split())

result1 = 0

while True:
    # n1이 k1으로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n1 // k1) * k1
    result1 += (n1 - target)
    n1 = target
    # n1이 k1보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n1 < k1:
        break
    # k1으로 나누기
    result1 += 1
    n1 //= k1
# 마지막으로 남은 수에 대하여 1씩 빼기
result1 += (n1 - 1)
print(result1)