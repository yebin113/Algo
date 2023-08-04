T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    for w in S:
        for i in range(int(R)):
            print(w,end='')

    print()
