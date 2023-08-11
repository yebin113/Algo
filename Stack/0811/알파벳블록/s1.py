N = int(input())
sen = []
sun_list = []
for i in range(N):
    btn = list(map(str, input().split()))
    if btn[0] == '1':
        sen.append(btn[1])
        sun_list.append(btn[1])
    elif btn[0] == '2':
        sen.insert(0, btn[1])
        sun_list.append(btn[1])
    else:
        if len(sen) != 0:
            sen.remove(sun_list.pop())
print(''.join(sen))
