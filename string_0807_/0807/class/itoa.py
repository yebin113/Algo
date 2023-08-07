"""
str() 함수를 사용하지 않고, itoa()를 구현해 봅시다.

양의 정수를 입력 받아 문자열로 변환하는 함수
입력 값 :변환할 정수 값, 변환된 문자열을 저장할 문자배열
반환 값 : 없음

hint = ord(), chr()
"""


def itoa_py(num):
    word = []
    if num > 0:  # 양수라면
        while num > 0:
            ascii_num = ord('0') + num % 10  # 1의 자리 숫자의 ascii code
            str_num = chr(ascii_num)  # 숫자의 아스키 코드를 다시 문자로 변경
            word.append(str_num)  # 리스트에 str 형태가 된 숫자를 받음
            num //= 10
        word.reverse()
        ans = ''.join(word)

    elif num == 0:
        ans = '0'

    else:   # 음수라면
        num = -num
        while num > 0:
            ascii_num = ord('0') + num % 10  # 1의 자리 숫자의 ascii code
            str_num = chr(ascii_num)  # 숫자의 아스키 코드를 다시 문자로 변경
            word.append(str_num)  # 리스트에 str 형태가 된 숫자를 받음
            num //= 10
        word.reverse()
        ans = ''.join(word)

    return ans


print(itoa_py(120))
