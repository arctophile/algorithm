# swea_1861. 정사각형 방

# BFS

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = []
    p = [] # 경로 배열

    q.append([y, x])
    v[y][x] = 1
    p.append(arr[y][x])

    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] - arr[y][x] == 1:
                    q.append([ny, nx])
                    v[ny][nx] = 1
                    p.append(arr[ny][nx])

    return min(p), len(p) # 출발 번호, 방문 갯수

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    v = [[0]*n for _ in range(n)] # 방문 배열

    num, cnt = 0, 0
    for y in range(n):
        for x in range(n):
            if not v[y][x]:
                a, c = bfs(y, x)
                if c > cnt or (cnt == c and num > a):
                    num, cnt = a, c

    print(f'#{t} {num} {cnt}')