sen1 = ['']+list(input())
sen2 = ['']+list(input())
# print(sen1,sen2)
# sen2의 가로 길이 sen1의 세로길이의 dp 생성
dp = [['']*len(sen2) for _ in range(len(sen1))]

# 위에서 아래
for i in range(len(sen1)):
    # 왼쪽에서 오른쪽
    for j in range(len(sen2)):

        # 만약 같은 글자라면 대각선 전 글자에 dp에 더해준다
        if sen1[i] == sen2[j] :
            dp[i][j] += dp[i-1][j-1] + sen1[i]
        # 같은글자가 아닐때
        else:
            # 한칸 위의 글자와 한칸 왼쪽의 글자와 비교해서 큰것을 담아줌
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]


print(len(dp[-1][-1]))
if len(dp[-1][-1]) != 0:
    print(dp[-1][-1])



