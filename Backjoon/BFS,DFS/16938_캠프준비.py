"""
dfs 활용
인자로 step과 levels-> 고른 난이도 리스트를 넘겨주고 재귀형식으로
탐색한다
가지치기로 난이도의 합이 R보다 큰경우
지금까지 고른 난이도의 합과 아직 골라지지 않은 step의 난이도의 합이 L보다 작다면 return


"""

def dfs(step,levels):
    global cnt
    # step이 N보다 크면 return
    if step > N:
        return
    # 합이 R 보다 크면 return
    elif sum(levels) > R:
        return
    # 아직 골라지지 않은 step의 난이도의 합과 지금까지 고른 난이도의 합이
    # L보다 작다면 return
    elif sum(levels) + sum(arr[step-1:N]) < L:
        return
    # 만약 step이 끝까지 도달했을때
    elif step == N:
        # 조건에 맞다면 cnt += 1
        if L <= sum(levels) <= R and max(levels) - min(levels) >= X:
            cnt += 1
            # print(levels)
    # step이 끝까지 갈때까지 지금step을 포함한 경우, 안한경우를 재귀
    else:
        dfs(step+1,levels+[arr[step]])
        dfs(step + 1, levels)






N,L,R,X = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
dfs(1,[])
dfs(1,[arr[0]])
print(cnt)
