k, n = map(int, input().split())
s = [input() for i in range(n)]
set_s = list(set(s))
cnt = []
for i in range(len(set_s)):
    cnt.append([set_s[i], s.count(set_s[i])])
num = 0

for i in range(n):
    p = 0
    for j in range(len(set_s)):
        if s[i] == cnt[j][0]:
            c = cnt[j][1]
            p = j
            break
    if c == 1:
        num += 1
        print(s[i])
        if num == k:
            break
    else:
        cnt[p][1] -= 1

