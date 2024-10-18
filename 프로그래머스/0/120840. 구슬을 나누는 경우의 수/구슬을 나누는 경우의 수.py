from math import factorial as fact
def solution(balls, share):
    """
    nCr : n!/(n-r)!r!
    """
    return fact(balls)/fact(balls-share)/fact(share)