def solution(age):
    """아스키코드
    파이썬에서는 ord()와 chr() 함수를 통해 문자를 아스키코드로, 아스키코드를 문자로 변환 가능.
    age의 각 자리수 num에 대하여, chr(num+97)을 통해 알파벳 문자로 변형하고
    각 문자들을 연결한다.
    """
    # print(ord('a')) ==> a를 인코딩하면 97
    # print(chr(98)) ==> 아스키코드 98은 b의미
    answer =""
    while age:
        num = age%10
        char = chr(num+97)
        answer = char+ answer
        age = age//10
    return answer