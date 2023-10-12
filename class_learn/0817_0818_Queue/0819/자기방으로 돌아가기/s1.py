import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    move_list = []
    for i in range(N):
        s_to_e = list(map(int, input().split()))
        move_list.append(s_to_e)
    # move_list 는 현재 학생이 있는 위치와 가야할 방의 위치가 리스트 형태로 담겨있는 리스트
    # q는 현재 이동할 수 있는 학생들
    q = [move_list[0]]
    cnt = 1
    move_list = move_list[1:]
    while q:
        # 현재 이동할 수 있는 학생
        now = q.pop(0)
        if now[1] % 2 == 1:     # 홀수면
            now[1] += 1         # 하나 더 늘림 (못가는 범위 늘리려고)
        # 남은 애들중에 추가로 이동가능한 친구들을 물색
        for move in move_list:
            # 가려는 위치와, 지금 위치가 현재 이동하는 학생과 겹치면 못감
            if now[0] <= move[0] <= now[1] or now[0] <= move[1] <= now[1]:
                # 다음기회를 노리기
                cnt += 1

            else:
                # 이동 가능하면 현재 리스트에서 지우고 q에 넣습니다
                move_list.remove(move)
                q.append(move)

    print(f'#{tc} {cnt}')
