data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1


for i in range(0,len(data)-1):
    num1 = int(data[i])
    num2 = int(data[i+1])
    if num1 != num2:
        if num2 == 1 :
            count0 += 1
        else:
            count1 += 1

print(min(count1, count0))

# 다시 시도해보기
# 이런 로직을 짜는데 있어서 문제에서 주어진 조건을 이용해 어떻게 구현할 것인지 생각을 더 할 수 있어야한다.