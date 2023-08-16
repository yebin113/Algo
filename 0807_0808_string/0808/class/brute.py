# Target : 검색 대상 // Pattern : 검색 패턴

target = "SSAFY 10th Let's go!"
pattern = "go"


def bruteForce(pattern, target):
    N = len(target)  # 검색 대상의 길이
    M = len(pattern)  # 검색 패턴의 길이

    i = 0  # Target의 인덱스
    j = 0  # Pattern의 인덱스

    # 각 인덱스가 타겟과 패턴의 길이보다 작을동안
    while i < N and j < M:
        # 패턴과 다른곳을 발견했을때
        if target[i] != pattern[j]:
            # j만큼 온 상태에서 틀린곳을 발견함
            # 지금위치 - j + ladder2 가 다음위치
            i = i - j
            # 패턴이 다르다면 굳이 패턴을 +ladder2 시킬 필요가 없어서 뒤의 +1을 상쇄시켜줌
            j = -1      # 0으로 초기화 시켜줭 함

        # 패턴과 같을때
        # 패턴과 타겟을 둘다 증가시킴
        i += 1
        j += 1
    
    if j == M:
        # 패턴 인덱스 j가 패턴의 길이만큼 탐색이 된것 == 탐색성공
        return i-M
    
    else:
        # 패턴 인덱스가 패턴의 길이에 도달하지 못한것 == 탐색 실패
        return -1
    pass
