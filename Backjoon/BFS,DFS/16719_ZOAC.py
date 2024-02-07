def dfs(start, arr):
    if not arr:
        return
    min_arr = min(arr)
    idx = arr.index(min_arr)

    ans[start + idx] = min_arr
    print("".join(ans))
    dfs(start + idx + 1, arr[idx + 1:])
    dfs(start, arr[:idx])

arr = list(input())
ans = [""] * len(arr)
dfs(0, arr)