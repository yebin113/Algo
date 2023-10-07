import sys
from collections import deque
def holzzak(num):
    if num % 2 == 1:
        return False
    else:
        return True


N,K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

start = deque()
max_len = 0
# 아이디어
# 하나씩 돌아가면서 짝수가 시작되는 인덱스를 리스트에 저장
for i in range(N):
    if holzzak(arr[i]):
        start.append(i)
if len(start)==0 or len(start)==1:
    print(len(start))
else:
    for i in range(len(start)):
        idx = start.popleft()
        length = 1
        K1 = K
        # print('시작',idx)
        while idx < N:
            idx += 1
            if idx==N:
                max_len = max(max_len, length)
                break
            # 짝수가 들어오면 길이 변수를 늘림
            if holzzak(arr[idx]):
                length += 1
                # print('현재위치',idx, '짝수 들어옴 길이 ->',length)
            # K1가 0이 된 후 홀수가 들어오면 최대길이 갱신 후 탈출
            elif holzzak(arr[idx])== False and K1 == 0:
                max_len = max(max_len,length)
                # print('max_len : ' ,max_len)
                break
            # 홀수가 들어오면 K1를 하나씩 줄임
            elif holzzak(arr[idx])== False:
                K1 -= 1
                # print('현재위치', idx, '홀수 들어옴 길이 ->', length, '기회',K1)
    print(max_len)