N = int(input())
i = 1

while 1:
    if i ** 2 > N:
        break
    i += 1

dp = [num**2 for num in range(1,i+1)]
