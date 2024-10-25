def solution(n):
    for i in range(1,n+1):
        if i*i == n:
            return 1
    return 2

def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
