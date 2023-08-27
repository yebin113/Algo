import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    odd_arr = []
    even_arr = []
    res = []
    if N % 2 == 1:
        # 만약 N이 홀수이면,
        # 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.
        res.append(arr.pop(0))
    # 반을 나눠 차례로 각 덱에 추가한다
    for i in range(N//2):
        even_arr.append(arr[i])
        odd_arr.append(arr[i+N//2])
    # 홀수라면 홀수 덱을 먼저 차례로 쌓는다
    if N % 2 ==1:
        for i in range(N//2):
                res.append(odd_arr[i])
                res.append(even_arr[i])
    # 짝수라면 짝수덱을 먼저 차례로 쌓는다
    else:
        for i in range(N//2):
            res.append(even_arr[i])
            res.append(odd_arr[i])
    # 결과를 언패킹한다
    print(f'#{tc}',*res)