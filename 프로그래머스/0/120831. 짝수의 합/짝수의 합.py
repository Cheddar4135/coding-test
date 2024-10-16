def solution(n):
    """
    2+4+6+8+10+12+14+16+18
    항수 num : n//2
    등차수열 합공식: num*(2a+(num-1)d)/2 => num * (4 +(num-1)*2)/2

    """
    
    return sum(range(2,n+1,2))