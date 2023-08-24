bit = [0]*8
a = 149
i = 7
# 자릿수를 알때
while a >0:
    bit[i] = a%2    # 해당 위치 bit에 할당
    a//=2
    i -= 1  # 자릿수를 하나씩 빼줌
bit[i] = a
print(''.join(map(str,bit)))    # 하나로 합쳐서 출력