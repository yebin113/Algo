def one(num):
    if num in num_dict:
        return num_dict[num]

    elif num <= 1:
        return 1

    else:
        num_dict[num] = num * one(num - 1)
        return num_dict[num]


N = int(input())
orders = list(map(int, input().split()))
num_dict = {}


if orders[0] == 1:
    k = orders[1]
    numbers = [i for i in range(1, N + 1)]
    result = []

    for i in range(N):
        j = one(N - 1 - i)
        step = (k - 1) // j
        result.append(numbers[step])
        numbers.remove(numbers[step])
        k -= j * step

    print(*result)

else:
    permutation = orders[1:]
    sorted_permutation = sorted(orders[1:])
    result = 1

    for i in range(N):
        step = sorted_permutation.index(permutation[i])
        sorted_permutation.remove(permutation[i])
        j = one(N - 1 - i)
        result += j * step

    print(result)