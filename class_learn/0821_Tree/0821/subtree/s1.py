import sys
sys.stdin = open("input.txt")

T = int(input())


# 하위 트리의 노드 개수를 더해주는 함수
def find_node(N):
    global count_node
    # 양쪽이 다 차있을때
    if ch1[N] != 0 and ch2[N] != 0:
        # 노드 +2
        find_node(ch1[N])
        find_node(ch2[N])
        count_node += 2
    # 한쪽만 있을때
    elif ch1[N] != 0:
        find_node(ch1[N])
        count_node += 1



for tc in range(1, T+1):
    E, N = map(int,input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    # 부모 인덱스로 저장
    for i in range(E):
        p,c = arr[2*i], arr[2*i +1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    count_node = 1
    find_node(N)



    print(f'#{tc} {count_node}')