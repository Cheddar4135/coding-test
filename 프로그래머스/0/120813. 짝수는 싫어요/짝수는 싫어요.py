import numpy as np
def solution(n):
    """n 이하의 홀수 리스트를 반환한다.
    9   [1,3,5,7,9]
    2   [1]
    4   [1,3]
    
    1. 가장 쉬운 방법은 arange아닐까.
    """
    
    answer = np.arange(1,n+1,2).tolist()
    return answer