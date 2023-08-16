"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AYmbBnEa7eMDFAUe&type=PROBLEM&problemBoxTitle=EXTRAS&problemBoxCnt=7
"""
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    stick = list(input())
    total_stick_count = 0
    stick_count = 0
    i = 0
    while i < len(stick):
        if stick[i] == '(':
            # 레이저라면
            if stick[i+1] == ')':
                # print(f"{i}칸. 레이저입니다. 쌓인 쇠막대기 {stick_count}개를 자릅니다")
                total_stick_count += stick_count
                # 두칸 건너뛰어 검사해야됨
                i += 1

            # 쌓인 쇠막대기 라면
            else:
                # 쇠막대기 한칸 추가
                stick_count += 1

        # 쌓인 쇠막대기의 끝이라면
        else:
            # 쇠막대기 한칸 삭제
            stick_count -= 1
            # 총 합 막대 하나 추가
            total_stick_count += 1
        i += 1

    print(f'#{tc} {total_stick_count}')

