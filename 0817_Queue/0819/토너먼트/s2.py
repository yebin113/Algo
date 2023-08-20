import sys
sys.stdin = open('input.txt')


def RSP(A,B):
    # 인덱스(사람의 번호)를 받으면
    # 그에 해당하는 딕셔너리 값을 반환해 가위바위보시키고 승자를 리턴
    if card_dict[str(B)] - card_dict[str(A)] == 1 or card_dict[str(B)] - card_dict[str(A)] == -2:
        return B
    else:
        return A

# 승자의 숫자카드와 인덱스를 리턴
def devided(start,end):
    if start == end:
        return start
    middle = (start+end)//2
    start = devided(start,middle)
    end = devided(middle+1,end)

    return RSP(start,end)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))
    card_dict = {}
    for i in range(N):
        card_dict[str(i)] = cards[i]
    print(card_dict)
    print(devided(0,N-1))