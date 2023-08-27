import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    money = int(input())

    cnt1 = cnt2 = cnt3 = cnt4 = cnt5 = cnt6 = cnt7 = cnt8 = 0
    while money > 0:
        if money >= 50000:
            cnt1 += 1
            money -= 50000
        elif money >= 10000:
            cnt2 += 1
            money -= 10000
        elif money >= 5000:
            cnt3 += 1
            money -= 5000
        elif money >= 1000:
            cnt4 += 1
            money -= 1000
        elif money >= 500:
            cnt5 += 1
            money -= 500
        elif money >= 100:
            cnt6 += 1
            money -= 100
        elif money >= 50:
            cnt7 += 1
            money -= 50
        else:
            cnt8 += 1
            money -= 10
    print(f'#{tc}')
    print(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8)