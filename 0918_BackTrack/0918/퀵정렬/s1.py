import sys
sys.stdin = open("input.txt")


# 중간값을 찾는 과정
def partition(l,r):
    # 일단 주어진 길이에서 첫번째 인덱스가 피봇
    pivot = arr[l]
    # 검사 시작점은 그 다음부터
    l += 1
    while True:
        # l값이 피봇보다 작을때
        while arr[l] < pivot:
            # l을 계속 늘립니다
            l += 1
        # r값이 피봇보다 크다면
        while arr[r] > pivot:
            # r을 계속 줄입니다
            r -= 1
        # 엇갈린 경우 r이 pivot의 위치
        if l >= r:
            return r
        # 엇갈리지 않았다면 r값과 l값을 바꿔줍니다
        arr[l],arr[r]= arr[r],arr[l]




def quick(l,r):
    # 왼쪽이 오른쪽보다 커지면 종료
    if l >= r:
        return
    # 피봇 결정
    pivot = partition(l,r)
    # 시작과 pivot위치 바꿈
    arr[l],arr[pivot]= arr[pivot],arr[l]
    # 범위 나눠서 재귀
    quick(l,pivot)
    quick(pivot+1,r)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(0,N-1)
    print(f'#{tc} {arr[N//2]}')