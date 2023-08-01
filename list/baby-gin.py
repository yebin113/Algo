
T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))
    # 리스트화 시켜서 입력받음
    count_list = [0] * 12   # index 오류 방지
    triplet = 0
    run_data = 0

    # 카운트 정렬
    for a in arr:
        count_list[a] += 1
    i = 0
    print(count_list)
    while i < 10:

        # triplet 검사
        # 카운트 리스트의 원소가 3보다 크다면
        if count_list[i] >= 3:
            triplet += 1
            count_list[i] -= 3
            continue

        # run 검사
        if count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2] >= 1:
            run_data += 1
            count_list[i] -= 1
            count_list[i+1] -= 1
            count_list[i+2] -= 1
            continue

        i += 1

    # baby-gin 조건 충족시
    if run_data + triplet == 2:
        ans = 1
        
    else:
        ans = 0
        
    # print(f'#{tc} {ans}')

