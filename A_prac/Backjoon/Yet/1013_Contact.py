def find_pattern(sign, length):
    global check
    visited = [0]*length
    now = 0
    while now < length - 1:
        # 01 패턴
        if sign[now] == '0':

            # 0부터 시작하면 01
            visited[now] = 1
            now += 1

            # 다음 게 1이여야 패턴 성립
            if now <= length - 1 and sign[now] == '1':
                visited[now] = 1
                now += 1

            # 패턴이 아닐 경우 return
            else:
                check = False
                return

        # 100+1+ 패턴 분석
        else:

            visited[now] = 1
            now += 1
            zero_count = 0

            # 0의 연속 파악
            while now < length and sign[now] == '0':
                visited[now] = 1
                zero_count += 1
                now += 1

            # 적어도 2개의 0이 있지 않거나 now가 끝까지 도달하면 패턴 아님 return
            if zero_count < 2 or now == length:

                check = False
                return
            # 1의 연속 파악
            one_count = 0
            while now < length and sign[now] == '1':
                visited[now] = 1
                one_count += 1
                now += 1

            # 1이 2개 이상이고 지금 위치가 뒤에서 두칸 보다 앞이며 다음 패턴이 100+1+일때
            if one_count >= 2 and now + 2 < length and sign[now + 1] == '0':
                visited[now] = 0
                now -= 1
    # 무사히 끝나면 통과
    return


T = int(input())
for _ in range(T):
    wave = input()
    len_wave = len(wave)
    check = True
    # 맨 끝이 0으로 끝나거나 1로 시작하는데 2글자 이내면 무조건 아님
    # 3글자짜리 패턴도 없음
    if wave[-1] == '0' or (len_wave <= 2 and wave[0] == '1') or len_wave == 3:
        print('NO')

    else:
        find_pattern(wave, len_wave)

        if check:
            print('YES')
        else:
            print('NO')
