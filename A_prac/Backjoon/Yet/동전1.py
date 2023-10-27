n, k = map(int, input().split())
coin_values = []

for _ in range(n):
    coin_value = int(input())
    coin_values.append(coin_value)

coin_values.sort()

dp = [0]*n

for i in range(n-1,-1,-1):
