# swea_1220. [S/W 문제해결 기본] 5일차 - Magnetic (제출용) D3

T = 10

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0 # 교착 상태 개수
    for x in range(n):
        top = 0 # n극 방향의 자성 물질 설정
        for y in range(n):
            if arr[y][x]: # n극 성질 물질이나 s극 성질 물질이면
                bot = arr[y][x] # s극 방향의 자성 물질
                if top == 1 and bot == 2: # 교착 상태 조건
                    cnt += 1
                top = arr[y][x] # n극 방향의 자성 물질 갱신

    print(f'#{t} {cnt}')