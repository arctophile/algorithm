# swea_1860. 진기의 최고급 붕어빵 (제출용) D3

T = int(input())

for t in range(1, T+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split())) # 도착 시간

    lst.sort()

    res = 'Possible'
    for i in range(len(lst)):
        b = (lst[i]//m)*k # 도착 시간의 제품 갯수(b), 도착 시간(lst[i])
        if b < i+1: # 도착 시간의 제품 갯수(b) < 도착 인원(i+1)
            res = 'Impossible' # 지연 발생
            break

    print(f'#{t} {res}')