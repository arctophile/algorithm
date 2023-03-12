# swea_12712. 파리퇴치3 (제출용) D2

dc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향 배열(+)
dx = [(-1, 1), (1, 1), (1, -1), (-1, -1)] # 방향 배열(×)

T = int(input())

for t in range(1, T+1):
   n, m = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(n)]

   Max = -int(21e8)

   for y in range(n):
       for x in range(n):
           sum = arr[y][x]
           for i in range(4):
               for j in range(1, m):
                   ny, nx = y + dc[i][0]*j, x + dc[i][1]*j # ＋ 형태 분사
                   if 0 <= ny < n and 0 <= nx < n:
                       sum += arr[ny][nx]

           if sum > Max:
               Max = sum

           sum = arr[y][x]
           for i in range(4):
               for j in range(1, m):
                   ny, nx = y + dx[i][0]*j, x + dx[i][1]*j # × 형태 분사
                   if 0 <= ny < n and 0 <= nx < n:
                       sum += arr[ny][nx]

           if sum > Max:
               Max = sum

   print(f'#{t} {Max}')