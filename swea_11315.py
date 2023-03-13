# swea_11315. 오목 판정 (제출용) D3

# 1

dy = [-1, 0, 1, 1]
dx = [1, 1, 1, 0]

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    res = 'No'
    for y in range(n):
        for x in range(n):
            for i in range(4):
                cnt = 0
                for j in range(5):
                    ny = y + dy[i]*j
                    nx = x + dx[i]*j
                    if 0 <= ny < n and 0 <= nx < n:
                        if arr[ny][nx] == 'o':
                            cnt += 1

                if cnt >= 5:
                    res = 'Yes'

    print(f'#{t} {res}')

# 2

T = int(input())

for t in range(1, T+1):
   n = int(input())
   arr = [list(input()) for _ in range(n)]

   trs = list(zip(*arr))

   res = 'No'

   for y in range(n): # y=0 오목 여부 확인
       s = ''
       for x in range(n):
           s += arr[y][x]

       if 'ooooo' in s:
           res = 'Yes'
           break

   for y in range(n): # x=0 오목 여부 확인
       s = ''
       for x in range(n):
           s += trs[y][x]

       if 'ooooo' in s:
           res = 'Yes'
           break

   flag = 0
   for y in range(n): # y=-x 오목 여부 확인
       for x in range(n):
           s = ''
           for i in range(n):
               ny, nx = y + 1*i, x + 1*i
               if 0 <= ny < n and 0 <= nx < n:
                   s += arr[ny][nx]

           if 'ooooo' in s:
               res = 'Yes'
               flag += 1
               break

       if flag:
           break

   flag = 0
   for y in range(n):  # y=x 오목 여부 확인
       for x in range(n):
           s = ''
           for i in range(n):
               ny, nx = y + 1*i, x - 1*i
               if 0 <= ny < n and 0 <= nx < n:
                   s += arr[ny][nx]

           if 'ooooo' in s:
               res = 'Yes'
               flag += 1
               break

       if flag:
           break

   print(f'#{t} {res}')