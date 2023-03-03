# swea_4613. 러시아 국기 같은 깃발 D4

# 1

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    f = [list(input()) for _ in range(n)]

    Min = int(21e8)
    for w in range(1, n-1):
        for b in range(1, n-1):
            for r in range(1, n-1):
                if w + b + r == n:
                    cnt = 0
                    for i in range(len(f)):
                        if 0 <= i < W:
                            cnt += (f[i].count('B') + f[i].count('R'))
                        elif W <= i < W+B:
                            cnt += (f[i].count('R') + f[i].count('W'))
                        else: # W+B <= i < W+B+R
                            cnt += (f[i].count('W') + f[i].count('B'))

                    if cnt < Min:
                        Min = cnt

    print(f'#{t} {Min}')

# 2

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    f = [list(input()) for _ in range(n)]

    Max = -int(21e8)
    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0
            for k in range(i+1):
                cnt += f[k].count('W')
            for k in range(i+1, j+1):
                cnt += f[k].count('B')
            for k in range(j+1, n):
                cnt += f[k].count('R')

            if cnt > Max:
                Max = cnt

    print(f'#{t} {n*m-Max}')