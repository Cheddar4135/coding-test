def solution(n):
    for i in range(1,11):
        if factorial(i)>n:
            return i-1
        elif factorial(i)==n:
            return i
def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans*=i
    return ans