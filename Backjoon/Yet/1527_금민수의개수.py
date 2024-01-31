from itertools import product
a,b = map(int,input().split())
cnt = 0
n = ['4','7']
for i in range(len(str(a)),len(str(b))+1):
    for num_list in product(n,repeat=i):
        num = ''.join(list(num_list))
        if int(num) < a:
            continue
        elif int(num) > b:
            break
        cnt += 1


print(cnt)