data = list(map(int, input().split()))
print((data[0]**2+data[1]**2+data[2]**2+data[3]**2+data[4]**2)%10)

# 좋은 코드 아님
# for문을 돌려야 유지보수가 쉽다.
# 나중에 입력값 10000개면 우짤거냐
# 위에 강씨 추천코드임
