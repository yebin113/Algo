import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    S1 = 13
    D1 = 13
    H1 = 13
    C1 = 13
    #  각 카드는 TXY 꼴로 표현되며,
    # T는 카드의 무늬(S, D, H, C)이며 XY는 카드의 숫자 (01 ~ 13)이다
    s = list(map(str, input()))
    # 중복 처리하기 위해 세트 사용

    card_set = set()
    # 세글자씩 나눠서 카드 정보 넣기
    for i in range(len(s)//3):
        card_set.add(''.join(s[3*i:3*i+3]))
    # 중복이 있으면 에러
    if len(card_set) != len(s)//3:
        print(f'#{tc} ERROR')
    else:
        for i in range(4):
            card = card_set.pop()

            if card[0] == 'S':
                S1 -= 1
            elif card[0] == 'D':
                D1 -= 1
            elif card[0] == 'H':
                H1 -= 1
            else:
                C1 -= 1
        print(f'#{tc} {S1} {D1} {H1} {C1}')

    #  문자열 S를 보고 지금 무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족한지 출력
