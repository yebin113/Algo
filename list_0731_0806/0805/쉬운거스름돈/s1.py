import sys
sys.stdin = open("input.txt")

T = int(input())

def func(N,money):   # 해당 단위의 돈이 최대로 거슬러질 수 있는 수
    answer = 0      # 갯수는 처음에 0개
    while N >= money:   # 만약 주어진 거스름 돈이 해당 단위의 돈보다 크거나 같으면(거슬러줄수 있으면)
        N -= money  # 해당 단위의 돈을 빼고
        answer += 1     # 카운트를 늘립니다
    return answer   # 카운트를 리턴


for tc in range(1, T+1):
    N = int(input())        # 거슬러 줘야 하는 거스름돈
    ans = []    # 거스름 돈 갯수 리스트

    # 우선 거스름돈 단위가 들어간 리스트를 만들고 싶어요.
    money = 50000       # 돈의 단위를 나눠서 리스트화 시키고 싶음(그냥 입력해도 되지만,,반복문 익숙해지기 위해)
    money_won = []      # 거스름 돈 단위가 들어간 리스트 초기화를 해줍니다
    # 돈 단위 리스트
    while money >= 10 :     # 돈의 단위의 마지막은 10원~
        if str(money)[0] == '알파벳블록':    # 만약 돈이 알파벳블록 단위라면? -> 오십원, 오백원, 오천원, 오만원
            money_won. append(int(money))   # 우선 단위 리스트에 추가
            money /= 5     # 그리고 5로 나누어 갱신 (-> 다음 단위는 천원, 만원, 십원 등등 이니깐..)
        else:       # 만약 돈의 앞자리수가 1이면
            money_won.append(int(money))        # 우선 단위 리스트에 추가
            money /= 2      # 2로 나누어 갱신 ( -> 다음 리스트는 앞자리 수 5단위니깐)
    # 돈 단위를 리스트화 시켰습니다.

    # 이제 주어진 거스름돈을 최소 갯수로 나누어 주는 파트 구현

    for i in money_won:     # 돈 단위 리스트를 순회하며
        ans.append(func(N, i))  # 위에 func 함수 사용
        N -= i * func(N, i)     # 그리고 거스름돈을 갱신
    print(f'#{tc}')
    print(*ans)