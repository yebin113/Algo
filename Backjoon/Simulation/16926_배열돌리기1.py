#
#
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# N,M,R = map(int,input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int,input().split())))
# visited = [[0]*M for _ in range(N)]
# shells = []
# i,j = 0,0
# while sum(sum(visited,[])) != N*M:
#     shell = []
#     for i in range