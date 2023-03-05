# swea_1238. [S/W 문제해결 기본] 10일차 - Contact

# BFS

def bfs(n):
    q = []
    v = [0]*101  # 방문 배열, 연락 받았으면 1 이상(받은 순서), 연락 받지 못했으면 0

    q.append(n)
    v[s] = 1

    while q:
        fr = q.pop(0)

        for to in arr[fr]:
            if not v[to]:
                q.append(to)
                v[to] = v[fr] + 1

    Max, idx = -int(21e8), 0 # 받은 순서, 받은 사람
    for i in range(1, 100+1): # 연락 번호 1 이상 100 이하
        if v[i] >= Max:
            Max, idx = v[i], i

    return idx

T = 10

for t in range(1, T+1):
    n, s = map(int, input().split()) # 인풋 길이, 시작 당번
    lst = list(map(int, input().split())) # 연락 정보

    arr = [[] for _ in range(101)]
    for i in range(0, n, 2):
        fr, to = lst[i], lst[i+1]
        arr[fr].append(to)

    res = bfs(s)

    print(f'#{t} {res}')