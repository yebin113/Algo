import sys
sys.stdin = open('input.txt')


def RSP(A,B):       # 가위바위보의 승자를 리턴
    if B - A == 1 or B - A == -2:
        return B
    else:
        return A


def card_game(start,end):
    if start == end:
        return card_name_list[start][0]
    middle = (start + end)//2
    start = card_game(start,middle)
    end = card_game(middle+1,end)
    return RSP(card_name_list[start][0],)


T = int(input())
for tc in range(1,T+1):
    # 인원수 N
    N = int(input())
    # N명이 고른 카드가 번호순으로 주어짐
    cards = list(map(int,input().split()))
    card_name_list = []     # N명의 번호와 고른 카드를 받는 리스트
    for i in range(N):
        card_name_list.append(i+1, cards[i])

    card_game(0,N-1)

    print(f'#{tc} ')