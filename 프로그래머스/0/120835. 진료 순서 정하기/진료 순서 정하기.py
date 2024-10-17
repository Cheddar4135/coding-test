def solution(emergency):
    """
    1. sorted()와 list.sort()
    >sorted()는 파이썬 내장함수로 인자로 모든 iterable이 올 수 있다. 정렬된 iterable을 반환한다.
    >list.sort()는 리스트만 사용가능하며, 리스트 자체를 변경하고 None을 반환한다.
    
    2. 인덱스 찾기: a.find()와 a.index()
    >find()는 문자열 메서드로 리스트, 튜플, 딕셔너리 자료형에서 사용 시 에러 발생한다.
    찾는 값이 없을 경우 -1을 리턴한다.
    >index()는 문자열, 리스트, 튜플 모두 사용가능하지만, 찾는 값이 없을 경우 ValueError 에러발생
    
    """
    ordered = sorted(emergency,reverse=True)
    return [ordered.index(i)+1 for i in emergency]

def solution(emergency):
    """딕셔너리 사용해 O(n)으로 time complexity줄이기인데 사실 이해안감
    """
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    for e in emergency:
        answer.append(emer_ls[e])
    return answer
