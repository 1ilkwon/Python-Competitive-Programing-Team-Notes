N, M = map(int,input().split())
data1 = list(map(int,input().split()))
result = 0

for i in range(0, len(data1)):
    for j in range(0, len(data1)):
        if data1[i] != data1[j] and data1[i] > data1[j] :
            result += 1

print(result)

'''
직접 푼 방식
위 방식은 주어진 입력값을 모두 사용하지 않은 코드이다.
또한 O(n^2)이라는 시간복잡도가 발생한다.
'''

n, m = map(int, input().split())
data = list(map(int,input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result1 = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m +1 ):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result1 += array[i]
print(result1)

'''
그리드를 할 때 어떤 것을 관점으로 매번 좋은것을 선택할지 고민해보자
'''