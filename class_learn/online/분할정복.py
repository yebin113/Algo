def f1(b, e):
    global cnt1

    if b == 0:
        return
    r = 1
    for i in range(e):
        r *= b
        cnt1 += 1
    return r


def f2(b, e):
    global cnt2

    if b == 0 or e == 0:
        return 1
    if e % 2:  # 홀수면
        r = f2(b, (e - 1) // 2)
        cnt2 += 1
        return r * r * b
    else:  # 짝수면
        r = f2(b, e // 2)
        cnt2 += 1
        return r * r
cnt1 = 0
cnt2 = 0
print(f1(2,20),cnt1)
print(f2(2,20),cnt2)