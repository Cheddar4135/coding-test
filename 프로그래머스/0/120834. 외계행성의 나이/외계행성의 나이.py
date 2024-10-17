def solution(age):
    """아스키코드
    파이썬에서는 ord()와 chr() 함수를 통해 문자를 아스키코드로, 아스키코드를 문자로 변환 가능.
    낮은 자리 수부터 age의 자리 수 num에 접근해, chr(num+97)을 통해 알파벳 문자로 변형하고
    각 문자들을 연결한다.
    print(ord('a')) ==> a를 인코딩하면 97
    print(chr(98)) ==> 아스키코드 98은 b의미
    """
    while age:
        num = age%10
        char = chr(num+97)
        answer = char+ answer
        age = age//10
    return answer

def solution(age):
    """ 내 코드 상위버전
    int를 iterable객체인 문자열로 바꿔 각 자리수에 높은자리부터 접근하고, 
    int형 타입으로 다시 바꾼다.
    거기에 97을 더해준 값을 다시 chr()함수를 통해 변환된 문자들이 담긴 리스트를
    ''.join()함수로 string으로 이어준다.
    """
    return ''.join([char(97+int(i))for i in str(age)])

def solution(age):
    """직관적 코드
    age를 문자열로 바꾼 후 0~9 문자를 a~j 문자로 치환한다.
    """
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

def solution(age):
    """dictory 이용 직관적 코드
    """
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
        ,'5':'f','6':'g','7':'h','8':'i','9':'j'}    
    return ''.join(conv[i] for i in str(age))
