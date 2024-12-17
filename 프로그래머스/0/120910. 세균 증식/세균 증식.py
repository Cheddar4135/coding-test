def solution(n, t):
    return n*2**t


def solution(n,t):
    #n의 비트를 왼쪽으로 t번 옮김. n * 2^t의미
    return n << t 

"""why it can be possible?
 비트 연산은 말그대로 비트를 움직이는 거다.
 비트를 왼쪽 또는 오른쪽으로 이동시키면 2를 곱하거나 나눈 효과가 나타난다.
"""
