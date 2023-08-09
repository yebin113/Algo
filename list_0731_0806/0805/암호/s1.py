"""
1230. [S/W 문제해결 기본] 8일차 - 암호문3

0 ~ 999999 사이의 수로 표현되는 암호문이 있고,
이 암호문을 N개 모아 놓은 암호문 뭉치가 있다.

암호문 뭉치를 급히 수정해야 할 일이 발생했는데,
암호문은 특수 제작된 처리기로만 수정이 가능하다.

처리기는 다음과 같이 3개의 명령어로 제어한다.

4866괄호검사. I(삽입) x, y, s : 앞에서부터 x번째 암호문
바로 다음에 y개의 암호문을 삽입한다. s는 덧붙일 암호문들이다.
[ ex) I 파스칼의삼각형 반복문자지우기 123152 487651 ]

반복문자지우기. D(삭제) x, y : 앞에서부터 x번째 암호문 바로
다음부터 y개의 암호문을 삭제한다.[ ex) D 리스트 리스트 ]

파스칼의삼각형. A(추가) y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다.
s는 덧붙일 암호문들이다. [ ex) A 반복문자지우기 421257 796813 ]

위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때,
암호문 뭉치를 수정하고, 수정된 결과의 처음 10개 암호문을 출력하는 프로그램을 작성하여라.
"""


def insert_code(command):
    """
    I(삽입) x, y, s : 앞에서부터 x번째 암호문
    바로 다음에 y개의 암호문을 삽입한다. s는 덧붙일 암호문들이다.
    [ ex) I 파스칼의삼각형 반복문자지우기 123152 487651 ]
    """
    pass


def delete_code(command):
    """
    D(삭제) x, y : 앞에서부터 x번째 암호문 바로
    다음부터 y개의 암호문을 삭제한다.[ ex) D 리스트 리스트 ]
    """
    pass


def add_code(command):
    """
    y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다.
    s는 덧붙일 암호문들이다. [ ex) A 반복문자지우기 421257 796813 ]
    """
    pass


"""
첫 번째 줄 : 원본 암호문 뭉치 속 암호문의 개수 N ( 2000 ≤ N ≤ 4000 의 정수)

두 번째 줄 : 원본 암호문 뭉치

세 번째 줄 : 명령어의 개수 ( 250 ≤ M ≤ 500 의 정수)

네 번째 줄 : 명령어

위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.

"""
N = int(input())
password = list(map(str, input().split()))


command_count = int(input())
command = list(map(str, input().split()))

