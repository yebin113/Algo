for tc in range(4):
    arr = list(map(int, input().split()))

    # A의 왼쪽 시작 x1 오른쪽 끝 x3
    # A의 아래쪽 시작 y1 위쪽 끝 y3
    A_x1 = arr[0]
    A_y1 = arr[1]
    A_x3 = arr[2]
    A_y3 = arr[3]
    # B의 왼쪽 시작 x1 오른쪽 끝 x3
    # B의 아래쪽 시작 y1 위쪽 끝 y3
    B_x1 = arr[4]
    B_y1 = arr[5]
    B_x3 = arr[6]
    B_y3 = arr[7]

    # 안겹침
    # x좌표 범위가 안맞거나 y좌표 범위가 안맞거나
    if A_x3 < B_x1 or B_x3 < A_x1 or A_y3 < B_y1 or B_y3 < A_y1:
        ans = 'd'

    # 한점이 같을경우 (왼위와 오아 또는 왼아와 오위가 같은 네가지경우만 꼽음)
    elif (A_x1 == B_x3 and A_y1 == B_y3) or \
            (A_x1 == B_x3 and A_y3 == B_y1) or \
            (A_x3 == B_x1 and A_y1 == B_y3) or \
            (A_x3 == B_x1 and A_y3 == B_y1):
        ans = 'c'
    # 한줄 겹침(안겹치거나 한점만 만나는 경우는 위에서 걸러져서 ㄱㅊ을듯)
    elif (A_x1 == B_x3) or \
            (B_x1 == A_x3) or \
            (B_y1 == A_y3) or \
            (A_y1 == B_y3):
        ans = 'b'

    # 나머지 경우
    else:
        ans = 'a'
    print(ans)
