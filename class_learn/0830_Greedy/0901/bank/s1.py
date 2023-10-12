import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    A = list(input())
    B = list(input())
    # 한글자씩 바꿀 이진수를 십진수로 변환한 값을 저장해둘 리스트
    binary = []
    for i in range(len(A)):
        cA = A[:]
        # 이진수 차례로 한글자씩 바꿔서 십진수로 변환해 저장
        cA[i] = str((int(cA[i]) +1)%2)
        binary.append(int(''.join(cA),2))

    # 삼진수도 한글자씩 바꾸는데 수의 범위가 3이니 한자리의 두번 확인이 필요
    for i in range(len(B)):
        cB1 = B[:]
        cB2 = B[:]
        # 자리를 바꾸고 이진수에 있는지 확인
        cB1[i] = str((int(cB1[i]) + 1) % 3)
        cb1 = int(''.join(cB1),3)
        if cb1 in binary:
            # 있다면 답 갱신
            ans = cb1
            break
        # 자리를 바꾸고 이진수에 있는지 확인
        cB2[i] = str((int(cB2[i]) + 2) % 3)
        cb2 = int(''.join(cB2),3)
        if cb2 in binary:
            ans = cb2
            break


    print(f'#{tc} {ans}')