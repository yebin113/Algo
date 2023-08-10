def LCM(A,B):
    while(B):
        A,B = B,A%B
    return A

A,B = map(int,input().split())
print(A*B//LCM(A,B))
