numbers = []
while True:
    a = list(map(int, input().split()))
    if a == [0, 0]:
        break
    numbers.append(a)
for number in numbers:
    if number[0] > number[1]:
        print("Yes")
        continue
    print("No")

# 다시 풀어볼것