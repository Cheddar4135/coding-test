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