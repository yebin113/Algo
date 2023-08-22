import sys
sys.stdin = open("input.txt")

# 후위 순회
def order(p,N):

    while p <= N:

        # 수식이 숫자면 변환해서 넣고 아니면 그냥 넣기
        try:
            yun = tree[p//2]
            if yun == '+':
                tree[yun] = int(tree[p-1]) + int(tree[p])
            elif yun == '-':
                tree[yun] = int(tree[p-1]) - int(tree[p])
            elif yun == '*':
                tree[yun] = int(tree[p-1]) * int(tree[p])
            elif yun == '/':
                tree[yun] = int(tree[p-1]) / int(tree[p])
            return tree

        except:
            return f'잘못되었습니다. {p}, {tree[p]}'




T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] *(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(N):
        arr = list(map(str,input().split()))
        tree[int(arr[0])] = arr[1]

        # 부모인덱스에 자식인덱스 저장하기
        # 4개를 받으면 두 자식 저장
        if len(arr) == 4:
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        # 3개 받으면 한자식만 저장
        elif len(arr) == 3:
            ch1[int(arr[0])] = int(arr[2])


    print(f'#{tc} {order(2,N)}')