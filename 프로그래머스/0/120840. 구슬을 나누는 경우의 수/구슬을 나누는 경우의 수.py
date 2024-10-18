from math import factorial as fact
import math

def solution(balls, share):
    """치사방법1. math모듈쓰기
    nCr : n!/(n-r)!r!
    """
    return fact(balls)/fact(balls-share)/fact(share)

def solution(balls,share):
    """더 치사한 방법2: math.comb쓰기
    """
    return math.comb(balls,share)
    
def fact(n):
    """factorial 재귀적으로 구현하기
    문제: 몇가지 케이스에서 runtime 에러 발생
    원인:  스택 깊이 초과 Stack Overflow Error
    해결 : 그냥 for문으로 풀 수 있는 건 for문으로 풀자.
    """
    if n==1:
        return 1
    else:
        return n*fact(n-1)

def fact(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
