k, n = map(int, input().split())
d = {}
for i in range(n):
    d[input()] = i

l = list(zip(d.keys(),d.values()))

sorted_l = sorted(l,key=lambda x:x[1])

if k > len(sorted_l):
    k = len(sorted_l)
for i in range(k):

    print(sorted_l[i][0])
