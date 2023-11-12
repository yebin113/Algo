# def find_efficient_line(now_lamp):
#     """
#     효율적인 열을 찾는 함수
#     각 열마다 켜져있는 불을 더한 후 가장 적게 켜진 곳을 고른다
#     :param now_lamp: 지금 lamp상태
#     :return: 효율적인 열
#     """
#     line_cnt = [0]*M
#     for i in range(N):
#         # 가망 없는 행은 건너뛰기
#         if i in count_k_more:
#             continue
#         for j in range(M):
#             # 현재 열마다 켜져있는 곳을 더한다
#             line_cnt[j] += lamp[i][j]
#     #     print('현재 행',lamp[i])
#     #     print('라인 합',line_cnt)
#     # print(line_cnt)
#     return line_cnt.index(min(line_cnt))
#
# def toggle_lamp(m):
#     """
#     효율적인 열을 받으면 해당 열을 토글해주는 함수
#     :param m: 효율적인 열
#     """
#     for i in range(N):
#         if lamp[i][m] == 0:
#             lamp[i][m] = 1
#         else:
#             lamp[i][m] = 0
#

N,M = map(int,input().split())
lamp = [list(map(int,input())) for _ in range(N)]
K = int(input())

cnt = 0
# 모든 행에 대해 반복
for i in range(N):
    # 0의 개수 세기
    zero_count = 0
    for num in lamp[i]:
        if num == 0:
            zero_count += 1
    same_col = 0
    # 0의 개수가 K개 이하
    if zero_count <= K and zero_count % 2 == K % 2:  # 이 행을 모두 킬 수 있다면
        for i2 in range(N):
            if lamp[i] == lamp[i2]:  # 두 개의 행이 같으면
                same_col += 1  # 1을 더해준다

    cnt = max(cnt, same_col)
print(cnt)
#
# count_k_more = []
# # 안켜진 불이 K개보다 많은 행들을 저장
# for i in range(N):
#     # k번으로 안켜지는 행들
#     if lamp[i].count(0) > K:
#         count_k_more.append(i)
#
# # 한번씩 클릭하는거보다 많이 해야 할때
# while K > M:
#     K -= 2
#
# # K번동안 효율적인 열을 찾고, 토글한다
# for k in range(K):
#     less_line = find_efficient_line(lamp)
#     toggle_lamp(less_line)
#
# # 켜져있는 행을 세는 변수
# cnt = 0
# for i in range(N):
#     if sum(lamp[i]) == M:
#         cnt += 1

