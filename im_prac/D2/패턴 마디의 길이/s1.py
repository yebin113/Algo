import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    arr = list(input())


    # 반복 패턴 길이 m
    for m in range(1,11):
        flag = True
        ans = 0
        # 해당 문장을 순회하기
        for i in range(m):
            # print(i, m, arr[i])
            ans += 1
            # 반복되는 구간만큼 돌아가면서 같은지 판단
            if arr[i] != arr[i+m]:
                flag = False
                # print('반복되지 않습니다..')
                break
        if flag == True:
            # print(f'답은 {m}입니다')
            break

    print(f'#{tc} {ans}')