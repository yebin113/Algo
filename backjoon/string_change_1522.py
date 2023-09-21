S = list(input())

# b의 첫등장
b_idx = S.index('b')
now = b_idx

# 이동할 인덱스
now += 1
while now != b_idx:
    # 리턴...
    if now == len(S):
        now = 0
