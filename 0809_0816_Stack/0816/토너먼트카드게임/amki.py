import sys

sys.stdin = open("input.txt")

T = int(input())

def RSP(A,B):
    if RSP_dict[A] == 1 and RSP_dict[B] == 2:
        return B
    elif RSP_dict[A] == 2 and RSP_dict[B] == 3:
        return B
    elif RSP_dict[A] == 3 and RSP_dict[B] == 1:
        return B
    # 동점인 경우도 그냥 빠른 번호로 출력
    else:
        return A


def divided(start, end):
    if start == end:
        return start
    mid = (start + end)//2
    start = divided(start,mid)
    end = divided(mid+1,end)
    return RSP(str(start),str(end))



for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    RSP_dict = {}
    for i in range(N):
        RSP_dict[str(i+1)] = arr[i]     # 순번대로 무슨 카드를 냈는지
    divided(1,N)

    print(f'#{tc}',divided(1,N))