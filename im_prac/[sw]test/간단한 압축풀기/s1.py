import sys
sys.stdin = open("input.txt")
"""
원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. 
(예 : A 5    AAAAA)
압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.
"""
T = int(input())

for tc in range(1, T+1):
    # 압축파일 개수
    N = int(input())
    print(f'#{tc}')
    # 압축 풀 리스트
    zipoff = []
    # 압출 풀기 실행할 횟수
    for i in range(N):
        # 압축된 글자와 압축된 양
        word, num = map(str,input().split())
        # 압축된 만큼 단어를 추가해준다
        for j in range(int(num)):
            zipoff.append(word)

    while 1:
        try:
            # 10개씩 끊어서 pop하여 출력
            for k in range(10):
                print(zipoff.pop(0),end='')
            # 10개 끝나면 한줄 띄기
            print()
        # pop할 거리없으면 탈출~
        except:
            print()
            break

