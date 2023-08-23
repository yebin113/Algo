"""
1번 풀이
- for i N 속에 for j N
- 두 숫자의 곱을 담은 리스트애 추가
- 제곱이면 뺌(다른 수를 곱해야하기 때문)
- 곱한 숫자 리스트를 순회합니다
- 해당 요소 하나 하나를 다시 숫자 리스트로 변환
- 정렬을 시킨 리스트와 현재 리스트가 같으면 단조 리스트에 추가
- 단조 리스트 중 가장 큰 값이 답입니다
=> 런타임 오류 ;;
2번 풀이
- for i N 속에 for j (i+길찾기,N)
- arr[i]와 arr[j]의 곱을 바로 자릿수 리스트로 만듦
- 해당 리스트가 sort 된 리스트와 동일할때
- 단조 리스트에 담음
- 단조 리스트 중 가장 큰값이 답입니다 
=> 런타임 오류 43개/50개
3번 풀이
- for i N 속에 for j (i+길찾기,N)
- arr[i]와 arr[j]의 곱을 바로 자릿수 리스트로 만듦 + res는 True
- 해당 리스트를 순회하면서 뒷자리 요소가 앞자리보다 작을때 res False로 바꾸고 break
- res 가 True일때 단조 리스트에 담음
- 단조 리스트 중 가장 큰값이 답입니다
=> 축하합니다 pass입니다
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 단조인 수를 넣을 리스트
    dan_list = []
    for i in range(N):
        for j in range(i+1,N):
            # 깃발세우기
            res = True
            # 주어진 배열에서 두 숫자를 뽑아서 곱한 값을 자릿수 리스트화 시킨것
            a = list(map(int,str(arr[i] * arr[j])))
            for k in range(len(a)-1):
                # 각 자리수 리스트를 순회하면서 뒷자리가 앞자리보다 작으면
                if a[k] > a[k+1]:
                    # 깃발을 내리고 탈출
                    res = False
                    break
            # for문이 끝나도록 깃발이 걸려있으면 단조리스트에 추가
            if res:
                dan_list.append(int(''.join(list(map(str, a)))))
    # 만약 단조 리스트가 0개면
    if len(dan_list) == 0:
        # -1출력
        print(f'#{tc} -길찾기')
    # 요소가 존재한다면
    else:
        # 가장 큰 값을 출력합니다
        print(f'#{tc} {max(dan_list)}')


"""
# 2번풀이..(실패힌것)

T = int(input())

for tc in range(길찾기, T + 길찾기):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    
    for i in range(N):
        for j in range(i+길찾기,N):
            a = list(map(int,str(arr[i] * arr[j])))
            if a == sorted(a):
                if max_num < int(''.join(list(map(str, a)))):
                    max_num = int(''.join(list(map(str, a))))

    if max_num == 0:
        print(f'#{tc} -길찾기')
    else:
        print(f'#{tc} {max_num}')



"""