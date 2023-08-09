for tc in range(4):
    arr = list(map(int, input().split()))

    set1 = set()
    set2 = set()
    # 각 직사각형 좌표 추가
    for i in range(arr[0], arr[2] + 1):
        for j in range(arr[1], arr[3] + 1):
            set1.add((i, j))

    for i in range(arr[4], arr[6] + 1):
        for j in range(arr[5], arr[7] + 1):
            set2.add((i, j))

    # 겹치는 구간 (교집합)
    set3 = set1 & set2
    N = len(set3)

    # 겹치는 구간 x랑 y좌표 따로 체크 중복되는 값 체크하기 귀찮아서 세트 사용
    x_set = set()
    y_set = set()
    for i in range(N):
        # 랜덤으로 겹치는 구간 좌표 하나를 빼서
        tuple1 = set3.pop()
        # 각각 x랑 y 좌표 넣는곳에 넣음
        x_set.add(tuple1[0])
        y_set.add(tuple1[1])
    # 만약 x좌표들의 집합이나 y좌표들의 집합의 길이가 둘중 하나라도 1이면 한줄겹침 b
    if len(x_set) == 1 or len(y_set) == 1:
        ans = 'b'
    # 둘다 아니면 직사각형 겹침
    else:
        ans = 'a'
    # 교집합 세트가 0개면 안겹침 d
    if N == 0:
        ans = 'd'
    # 교집합 좌표가 한개면 한점겹침 c
    elif N == 1:
        ans = 'c'
    print(ans)
