data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 막힌 부분

# data를 input()으로 받았다.
# input은 자료형을 문자열로 받는다.

# data를 문자열로 받기 때문에 이를 integer해주어 특정 변수에 저장하여 관리하는 것도 방법이다. 일일이 data[i]하지말고

# 만약 첫 글자가 0이거나 1인 경우도 고려해야한다.