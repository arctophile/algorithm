# swea_1953. [모의 SW 역량테스트] 탈주범 검거

# BFS

d = [
    [-1, 0], # 0 : 북, 2 연결 필수
    [0, 1],  # 1 : 동, 3 연결 필수
    [1, 0],  # 2 : 남, 0 연결 필수
    [0, -1]  # 3 : 서, 1 연결 필수
] # 방향 배열

s = [
    [],
    [0, 1, 2, 3], # 타입 1
    [0, 2], # 타입 2
    [1, 3], # 타입 3
    [0, 1], # 타입 4
    [1, 2], # 타입 5
    [2, 3], # 타입 6
    [0, 3], # 타입 7
] # 터널 종류, 0 : 북, 1 : 동, 2 : 남, 3 : 서

def bfs(y, x, p):  # 세로 위치, 가로 위치, 경과 시간
    q = []
    v = [[0]*m for _ in range(n)] # 방문 배열

    q.append((y, x, p))
    v[y][x] = 1

    while q:
        y, x, p = q.pop(0)

        if p < l:  # 경과 시간 < 소요 시간
            for t in s[arr[y][x]]:
                ny, nx = y + d[t][0], x + d[t][1]
                if 0 <= ny < n and 0 <= nx < m: # 지하 범위 확인
                    if arr[ny][nx]:  # 터널 여부 확인
                        if not v[ny][nx]:  # 방문 여부 확인
                            if (t+2)%4 in s[arr[ny][nx]]:  # 연결 여부 확인
                                q.append((ny, nx, p+1))
                                v[ny][nx] = 1

    cnt = 0
    for y in range(n):
        for x in range(m):
            if v[y][x]:
                cnt += 1

    return cnt

T = int(input())

for t in range(1, T+1):
    n, m, r, c, l = map(int, input().split()) # 지하 터널 세로 크기, 지하 터널 가로 크기, 맨홀 뚜껑 세로 위치, 맨홀 뚜껑 가로 위치, 소요 시간
    arr = [list(map(int, input().split())) for _ in range(n)]

    res = bfs(r, c, 1)

    print(f'#{t} {res}')