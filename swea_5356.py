# swea_5356. 의석이의 세로로 말해요 (제출용) D3

T = int(input())

for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    str = ''
    for x in range(15): # 단어 길이 1 이상 15 이하
        for y in range(5):
            if x < len(arr[y]):
                str += arr[y][x]

    print(f'#{t} {str}')