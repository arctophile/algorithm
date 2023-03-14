# swea_6485. 삼성시의 버스 노선 (제출용) D3

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    arr = [[] for _ in range(n)] # row : 버스 노선, col : 버스 노선의 정차 위치
    for i in range(n): # 버스 노선
        a, b = map(int, input().split())
        arr[i] = list(range(a, b+1)) # 정차 위치 a 이상 b 이하

    p = int(input())

    lst = [0]*p # index : 정차 위치, lst[index] : 노선 개수
    for i in range(p):
        c = int(input()) # 정차 위치
        for j in range(n):
            if c in arr[j]:
                lst[i] += 1

    print(f'#{test_case}', *lst)