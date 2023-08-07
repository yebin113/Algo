s1 = 'abc'
s2 = 'abd'
print(s1 < s2)  # True
print(s1 > s2)  # False
print(s1 == s2)  # False
# 사전순

s3 = 'ABC'
print(s1 < s3)  # False
print(s1 > s3)  # True
print(s1 == s3)  # False
# 대문자가 아스키코드 앞쪽에 나와서 더 작음

s4 = 'abcd'
print(s1 < s4)  # True
print(s1 > s4)  # False
print(s1 == s4)  # False
# 같은 문자 + 알파가 붙으면 뒤에 문자가 붙은것이 더 높다.