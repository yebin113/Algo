s = 'Reverse'
s_list = list(s)
N = len(s)

for i in range(N // 2):
    s_list[i], s_list[N - 1 - i] = s_list[N - 1 - i], s_list[i]
print("".join(s_list))
