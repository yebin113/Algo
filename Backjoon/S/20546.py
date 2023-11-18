# 호재
# 한 번 산 주식은 절대 팔지 않는다
# 준현이는 주식을 살 수 있다면 무조건 최대한 많이 산다.
# 주식을 살 수 있다면 가능한 만큼 즉시 매수

def bnp(money):
    have = 0
    for i in range(len(stock_price)):
        if money < stock_price[i]:
            continue
        now = money // stock_price[i]
        have += now
        money -= now * stock_price[i]
        if money == 0:
            break
    return money + have * stock_price[-1]



# 성민
# 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도
# 전일과 오늘의 주가가 동일하다면 가격이 상승한 것이 아니다.
# 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정
# 주식을 전량 매수
# 2021년 1월 1일부터 2021년 1월 14일
def timing(money):
    up_down = [0]*len(stock_price)
    for i in range(1,len(stock_price)):
        # 상승
        if stock_price[i] > stock_price[i-1]:
            up_down[i] = 1
        # 하락
        elif stock_price[i] < stock_price[i-1]:
            up_down[i] = -1

    # print('업 다운',up_down)
    have = 0
    for i in range(2, 14):
        # print('현재 돈 ',money,'현재 갖고있는 주',have)
        # 3일 연속
        if up_down[i-2] == up_down[i-1] and up_down[i] == up_down[i-1]:
            # 상승이면
            if up_down[i] == 1:
                # 매도
                money += have * stock_price[i]
                have = 0
            elif up_down[i] == -1:
                # 매수
                all = money // stock_price[i]
                have += all
                money -= all * stock_price[i]

    return have * stock_price[-1] + money


seed_money = int(input())
stock_price = list(map(int,input().split()))
A = bnp(seed_money)
B = timing(seed_money)
# print(A, B)
if A > B :
    print("BNP")
elif A == B:
    print("SAMESAME")
else:
    print("TIMING")