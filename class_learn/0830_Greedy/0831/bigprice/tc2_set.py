# set -> 중복 검사 삭제
import sys
sys.stdin = open("input.txt")

T = int(input())
# 완전탐색, 가지치기
def back_track(repeat):
    global ans
    val = int(''.join(P))       # 숫자카드
    if val in visited[repeat]: #이미 체크가 완료된 패턴
        return
    visited[repeat].add(val) # 검사 전이라면 패턴을추가
    if repeat == r: # 교환 횟수까지 도달했다면
        ans = max(val,ans)  # 최대상금 갱신
    else:   # 교환횟수 남음
        for i in range(N-1):
            for j in range(i+1,N):
                # 변경하고
                P[i],P[j] = P[j],P[i]
                # 확인
                back_track(repeat+1)
                # 원상복구
                P[i],P[j] = P[j],P[i]

for tc in range(1, T+1):
    arr  = list(input().split())
    visited = [set() for _ in range(11)]        # 최대 교환이 10//set으로 중복삭제
    P , r = list(arr[0]),int(arr[1])    # 숫자 패턴 P, 교환횟수 r
    ans = 0
    N = len(P) # 숫자카드의 길이
    back_track(0)
    print(f'#{tc} {ans}')
