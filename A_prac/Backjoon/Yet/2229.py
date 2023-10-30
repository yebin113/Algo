# 첫째 줄에 N이 주어진다.
# 다음 줄에는 N명의 학생들의 점수가 나이 순서대로 주어진다.
# 각 학생의 점수는 0 이상 10,000 이하의 정수이다.
N = int(input())
point = list(map(int, input().split()))
"""
10
2 5 7 1 3 4 8 6 9 3
"""
start = 0
end = 1
while end <= N:
    end += 1
    arr = point[start:end]
    if len(arr) < 2:
        continue
    # 현재 점수
    jumsu = max(arr) - min(arr)
    arr2 = point[end:]
    if


















# # 1. 이분탐색 실패
# start = 0
# end = max(point) * N
# max_jumsu = 0
# while start <= end:
#     mid = (start + end) // 2
#     print(f'start {start},end {end} mid {mid}')
#     hap = 0
#     location = 0
#     for i in range(N):
#         arr = point[location:i + 1]
#         if max(arr) - min(arr) > mid:
#             hap += max(arr) - min(arr)
#             location = i + 1
#         print(
#             f'location: {location} i : {i} max(arr) : {max(arr)} - min(arr) : {min(arr)} = {max(arr) - min(arr)} hap {hap}')
#     if max_jumsu <= hap:
#         max_jumsu = hap
#         end = mid - 1
#     else:
#         start = mid + 1
#     print(f'start {start},end {end} mid {mid} max_jumsu {max_jumsu}')
# print(max_jumsu)
