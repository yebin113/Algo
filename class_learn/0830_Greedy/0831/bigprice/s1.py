import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 숫자판의 정보와 교환횟수
    board, N = map(str,input().split())
    N = int(N)
    n = N
    arr = list(map(int,board))
    flag = False

    # 카운트 세기
    count = [0]*10
    for i in range(len(arr)):
        count[arr[i]] += 1
    # 중복 있으면 깃발 올리기
    if max(count)>=2:
        flag = True

    # 시작 위치
    i = 0
    # 1. 우선 교환 횟수가 끝나거나 인덱스가 끝날때까지
    while N != 0 and i < len(arr)-1:
        max_num = 0
        max_idx = []
        min_num = 10
        min_idx = 0
        for k in range(i,len(arr)):
            # 최댓값이 여러개일때
            if max_num <= arr[k]:
                max_num = arr[k]
                if max_num == max(arr[i:]):
                    # 인덱스 저장
                    max_idx.append(k)

            # 최소가 아니라면
            if min_num > arr[k]:
                min_num = arr[k]
                min_idx = k

        # 만약 현재자리가 최대라면(바꿀필요가 없다면) 넘어감
        if max_num == arr[i]:
            i += 1
            continue
        # 중복된 값이 있고 교환 횟수가 2번 이상이지만 보드판갯수보다 작을때 현재가 가장 작은 값이 아니라면
        if len(max_idx)!= 1 and 2<=n<len(arr)-1 and min_idx != i:
            # 가장 작은 수가 아니면 남은 횟수만큼의 앞 최댓값이랑 자리를 바꾼다
            arr[i], arr[max_idx[len(max_idx)-1-N+1]] = arr[max_idx[len(max_idx)-1-N+1]], arr[i]
        else:
            # i번째 이후에서 최댓값과 현재 자리 i를 교환
            arr[i],arr[max_idx[-1]] = arr[max_idx[-1]],arr[i]

        # 교환 횟수 줄임
        N -= 1
        # 현재 위치 갱신
        i += 1



    # 2. 교환이 남아있다면
    while N != 0:
        # 만약 같은 수가 있다면..
        if flag:
            break
        # 없다면 맨 끝 두개만 바꾸기..
        else:
            arr[-1],arr[-2] = arr[-2],arr[-1]
            N -= 1


    print(f'#{tc}',end = ' ')
    for i in arr:
        print(i,end='')
    print()