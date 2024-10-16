def solution(n, k):
    """
    n//10개의 음료수는 공짜
    """
    dish = 12000
    drink = 2000
    return dish*n + drink*(k-n//10)