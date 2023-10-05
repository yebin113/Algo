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
    i = 0
    j = N-1
    while j-i+1 > K:
        if check(i,j):
            max_len = max(max_len,j-i+1)
            break


