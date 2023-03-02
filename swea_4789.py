# swea 4789. 성공적인 공연 기획 D3

# 1

T = int(input())

for t in range(1, T+1):
    s = input()

    sts, rqd = 0, 0 # 현재 인원(기립 박수), 고용 수요
    for i in range(len(s)): # i : s의 index
        if i > sts: # i : 조건 인원(기립 박수), 조건 인원 > 현재 인원
            rqd += (i - sts) # 고용 수요 += 추가 고용(= 조건 인원 - 현재 인원)
            sts += (i - sts + int(s[i])) # 현재 인원 += 인원 증분(기립 박수)(= 고용 증분 + 관객 증분)
        else: # 조건 인원 == 현재 인원
            sts += int(s[i]) # 현재 인원 += 인원 증분(기립 박수)(= 관객 증분)

    print(f'#{t} {rqd}')

# 2

T = int(input())

for t in range(1, T+1):
    s = input()

    sts, rqd = 0, 0 # 현재 인원(기립 박수), 고용 수요
    for i in range(1, len(s)+1): # i : 글자 번호
        if i-1 > sts: # i-1 : 인원 조건(기립 박수), 조건 인원 > 현재 인원
            rqd += ((i-1) - sts) # 고용 수요 += 추가 고용(= 조건 인원 - 현재 인원)
            sts += ((i-1) - sts + int(s[i-1])) # i-1 : 인원 조건, s[i-1]의 i-1 : s의 index, 현재 인원 += 인원 증분(기립 박수)(= 고용 증분 + 관객 증분)
        else: # 조건 인원 == 현재 인원
            sts += int(s[i-1]) # 현재 인원 += 인원 증분(기립 박수)(= 관객 증분)

    print(f'#{t} {rqd}')