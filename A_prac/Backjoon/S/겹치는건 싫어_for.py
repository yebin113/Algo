# 쭉하면서 카운트 세고 젤 많은거 K개 넘어가면 그 거부터 다시 시작!

from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().split()))
# 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이
max_len = 0
minus = [0] * N
# 한 숫자로 이루어진 경우 가지치기
if len(list(set(arr)))==1:
    print(K)
else:
    len_now = 0



