def solution(n):
    """n명이 6조각피자를 최소 몇판시켜야 모두 같은 수의 피자로 나눠먹을 수 있을까.
    (6*anw)을 n으로 나눴을때 나머지가 0이어야한다.
    제한사항: n은 100명까지. 피자개수는 최대 100

    """
    for i in range(1,101):
        if (6*i) % n ==0:
            return i

def solution:
    ans = 1
    while (6*i)%n:
        ans+=1
    return 
