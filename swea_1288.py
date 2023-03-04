# swea_1288. 새로운 불면증 치료법 D2

T = int(input())

for t in range(1, T+1):
    n = int(input())

    v = [0]*10 # 방문 배열(0부터 9까지), 숫자 등장하지 않았으면 0, 등장하면 1

    i = 0
    while 0 in v: # v 배열의 모든 인덱스의 값이 1이 되면 반복 종료
        i += 1
        for s in str(i*n): # s : i*n번 양의 각 자리수
            if not v[int(s)]: # v 배열의 s 인덱스의 값이 0이면
                v[int(s)] = 1 # v 배열의 s 인덱스의 값을 1으로

    print(f'#{t} {i*n}')