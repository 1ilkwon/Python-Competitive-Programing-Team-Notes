N, M = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(N)]
m = M
for i in range(0,N+1):
    for i in range(0,M+1):
        [N,M] == [N,m-i]
print(fish)