# 문자열 입력
S = list(input())
for i in range(len(S)):
    # 대문자일때
    if ord(S[i]) <= 90:
        # 소문자로 바꿔줌(아스키코드 조작으로)
        S[i] = chr(ord(S[i]) + 32)
# 중복 삭제된 알파벳
set_s = list(set(S))
# 각 알파벳 몇갠지 저장할 카운트
count_S = [0]*len(set_s)
# 각 알파벳이 몇개인지 저장합니다
for i in range(len(set_s)):
    count_S[i] += S.count(set_s[i])

# 카운트의 최대값
max_count = max(count_S)
# 최대값이 두개 이상이면 -> 물음표
if count_S.count(max_count) > 1:
    ans = '?'
# 최대 알파벳 개수가 하나라면
else:
    # 가장 많은 카운트 값의 인덱스를 구합니다
    max_count_idx = count_S.index(max(count_S))
    # 그 인덱스에 해당하는 set의 알파벳이 해당 문자열에서 가장 많은 알파벳입니다.
    max_alpha = set_s[max_count_idx]
    # 답을 대문자로 바꿔줍니다
    ans = max_alpha.upper()

print(ans)
