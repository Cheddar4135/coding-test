def solution(my_string):
    """리스트 슬라이싱 연산자 이용하기
    장점: 같은 원소들을 역방향으로 담고 있는 새로운 리스트 생성할 때 유용하다.
    """
    return my_string[::-1]
#  같은 원소를 역방향으로 담고 있는 동일한 크기의 리스트(여기서는 문자열)를 새로 만든다.



def solution_2(my_string):
    """reversed() 내장함수 이용하기
    인자: 리스트, 튜플, 문자열 가능
    기능: 주어진 자료구조에 담긴 원소들을 역순으로 순회할 수 있는 반복자(iterator)를 결과값으로 반환
    반환: 인자로 넘어온 자료구조 타입이 아니라 반복자 타입을 반환함 <reversed object>

    장점: 반복자로 반환하기 때문에 for문으로 루프 돌릴 때 메모리 사용량 측면에서 이점 있다.
     역방향으로 루프 돌리기 위해서 고안되었다고 말해도 과언이 아님
    (반복자는 미리 메모리에 모든 원소를 올려놓지 않고 필요할 때마다 원소를 하나씩 제공)
    
    예제: for i in reversed([1,2,3]): print(i)
    """
    """string.join(iterable) 함수
    string: sperator 기능. 반환되는 값들 사이를 채우는 문자열
    iterable: 반환된 모든 값이 하나의 문자열이 될 반복 가능한 객체
    *주의: 사전을 반복 가능한 객체로 사용할 때 반환되는 값은 값이 아닌 키이다.
    예제: x = "#".join(myTuple), x = mySeparator.join(myDict)
    """
        return ''.join(reversed(my_string))


def solution_3(my_string):
    """리스트의 reverse()함수 이용하기
    기능: 기존 리스트 내의 원소들을 제자리에서(in place) 역방향으로 재배치
    """
    my_list = list(my_string)
    my_list.reverse()

    answer = ''.join(my_list)

    return answer
