def solution(my_string):
    """기억나지? 아스키코드 변환
    ord()와 chr() 함수를 통해 문자를 아스키코드로, 아스키코드를 문자로 변환 가능.
    print(ord('a')) ==> a를 인코딩하면 97
    print(chr(98)) ==> 아스키코드 98은 b의미
    
    A~Z:65~90
    a~z:97~122
    """
    # print(ord('a'),ord('z'),ord('A'),ord('Z')) =====> 97,122,65,90
    # print(ord('a')-ord('A')) ===>32
    ans=''
    for char in my_string:
        if ord(char)<91:
            ans+=chr(ord(char)+32)
        else:
            ans+=chr(ord(char)-32)
    return ans


def solution(my_string):
    """
    더 설명력 좋은 코드 버전
    """
    ans =''
    for i in my_string:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            ans += chr(ord(i)-32)
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            ans += chr(ord(i)+32)
    return ans

def solution(my_string):
    """
    사실 문자열 메서드 쓰면 됨. 
    """
    ans = ''
    for char in my_string:
        if char.isupper():
            ans+=char.lower()
        else:
            ans+=char.upper()
    return ans
