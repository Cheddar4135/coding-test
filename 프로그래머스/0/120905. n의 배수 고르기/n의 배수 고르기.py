def solution(n, numlist):
    """
    numlist의 원소들 중 n으로 나눴을 때 나머지가 있는 녀석들을 제거해야하는 함수
    
    Q. 문제 발생, 나머지가 있는 v라면 numlist.pop(v)를 해줬는데 왜 제대로 모든 v가 삭제가 안될까?
    A. numlist를 순회하고 있는데 numlist의 원소를 삭제해버리면 순회가 이상하게 되지.
    생각보다 코드 짤 때 이런 경우에 대한 고민이 자주 생기는 것 같아.
    (looping되는 순회자를 순환문 안에서 건드는거)
    늘 조심해야지. 어쩔 수 없이 inplace는 어렵겠군
    """
    ans = []
    for v in numlist:
        if not v%n:
            ans.append(v)
    return ans