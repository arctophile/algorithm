# swea 5789. 현주의 상자 바꾸기 D3

T = int(input())

for t in range(1, T+1):
    n, q = map(int, input().split()) # n : 상자 개수, q : 수행 횟수

    box = [0]*(n+1)

    for i in range(1, q+1): # 1번째부터 q번째까지 작업 수행
        l, r = map(int, input().split())

        for j in range(l, r+1): # l번 상자부터 r번 상자까지 작업 번호로 숫자 변경
            box[j] = i

    print(f'#{t} ', end='')
    print(*box[1:]) # 1번 상자부터 n번 상자까지 번호 출력