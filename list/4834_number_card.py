"""
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    
    # 카운트 정렬 리스트 초기화
    count_list = [0] * 10
    
    # 카운트 정렬
    for a in arr:
        count_list[a] += 1
    
    # 가장 많은 개수를 저장할 변수와 가장 많은 수를 저장할 변수
    max_count = 0
    max_num = 0

    for i in range(10):
        # 최대 카운트와 그 수 저장
        if max_count <= count_list[i]:
            max_count = count_list[i]
            max_num = i

    print(f'#{tc} {max_num} {max_count}')
