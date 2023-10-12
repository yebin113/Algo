def recur_func(n):
    if n == 0:
        return
    print(n, end=' ')
    recur_func(n - 1)
    print(n, end=' ')


recur_func(5)
