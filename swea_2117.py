# swea_2117. [모의 SW 역량테스트] 홈 방범 서비스

# 1 : 반복

T = int(input())

for t in range(1, T+1):
   n, m = map(int, input().split()) # 도시 크기, 운영 비용
   arr = [list(map(int, input().split())) for _ in range(n)] # 도시 정보

   Max = -int(21e8)
   for y in range(n):
       for x in range(n):
           for k in range(1, 2*n):
               cnt = 0
               for r in range(y-k+1, y+k):
                   if 0 <= r < n:
                       for c in range(x-k+1+abs(r-y), x+k-abs(r-y)):
                           if 0 <= c < n:
                               cnt += arr[r][c]

               if k*k + (k-1)*(k-1) <= m*cnt:
                   Max = max(Max, cnt)

   print(f'#{t} {Max}')

# 2 : BFS

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y, x):
   q = []
   v = [[0]*n for _ in range(n)] # 0 : 방문하지 않았으면 0, 방문하면 1 이상(방문 배열 역할, 운영 영역 기록)

   q.append((y, x))
   v[y][x] = 1

   k, cnt, Max = 0, arr[y][x], -int(21e8)
   while q:
       y, x = q.pop(0)

       if k != v[y][x]:
           k = v[y][x]
           if k*k + (k-1)*(k-1) <= m*cnt:
               Max = max(Max, cnt)

       for i in range(4):
           ny, nx = y + dy[i], x + dx[i]
           if 0 <= ny < n and 0 <= nx < n:
               if not v[ny][nx]:
                   q.append((ny, nx))
                   v[ny][nx] = v[y][x] + 1
                   cnt += arr[ny][nx]

   return Max

T = int(input())

for t in range(1, T+1):
   n, m = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(n)]

   Max = -int(21e8)
   for y in range(n):
       for x in range(n):
           Max = max(Max, bfs(y, x))

   print(f'#{t} {Max}')

# 3 : 구현

def fun():
   h = [] # 건물 좌표
   for y in range(n):
       for x in range(n):
           if arr[y][x]:
               h.append((y, x))

   Max = 0
   for y in range(n):
       for x in range(n):
           d = [0]*40 # 기준 위치에서 주택 좌표까지 거리 기준 건물 갯수
           for dy, dx in h:
               t = abs(y-dy) + abs(x-dx) + 1
               d[t] += 1

           for k in range(1, 40):
               d[k] += d[k-1] # 운영 영역 내부의 누적 건물 갯수
               if (k*k) + (k-1)*(k-1) <= m*d[k]:
                   Max = max(Max, d[k])

   return Max

T = int(input())

for t in range(1, T+1):
   n, m = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(n)]

   res = fun()

   print(f'#{t} {res}')