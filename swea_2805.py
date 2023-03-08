# swea_2805. 농작물 수확하기 (제출용) D3

# 1 : 규칙

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    inc = 0
    for y in range(n):
        for x in range(abs(n//2-y), n-abs(n//2-y)):
            inc += arr[y][x]

    print(f'#{t} {inc}')

# 2 : 범위

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    start, stop, inc = n//2, n//2+1, 0
    for y in range(n):
        for x in range(start, stop):
            inc += arr[y][x]

        if y < n//2:
            start -= 1
            stop += 1
        else:
            start += 1
            stop -= 1

    print(f'#{t} {inc}')