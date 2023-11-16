# 슬라이싱 대체 뭘로 하지..............
# 카운트는 set로 필요한 값만 카운트 -> 2%

# 수열 중복 체크
def check(i, j):
    arr1 = arr[i:j+1]
    check_set= list(set(arr1))
    for m in check_set:
        if arr1.count(m) > K:
            return False
    return True


def make_suyeul(i, j):
    global max_len
    # K개 이하로 줄어들면 탈출
    # 기존 값보다 작으면 탈출(가지치기)
    if i == j+K or j - i < max_len:

        return
    # print(i,j)

    # 수열중복체크에 통과하면
    if check(i, j):
        # max_len 갱신
        max_len = max(max_len, j + 1 - i)
        return
    else:
        # 앞에서 가는거
        if minus[i] == 0:
            minus[i] = 1
            make_suyeul(i + 1, j)
            minus[i] = 0
        # 뒤에서 오는것
        if minus[j] == 0:
            minus[j] = 1
            make_suyeul(i, j-1)
            minus[j] = 0

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
    make_suyeul(0, N - 1)
    print(max_len)