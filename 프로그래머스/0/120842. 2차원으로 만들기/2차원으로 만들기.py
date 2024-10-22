import numpy as np
def solution(num_list, n):
    a = np.array(num_list)
    return a.reshape(-1,n).tolist()

def solution(num_list, n):
    """다른사람풀이
    약간 반성되네..
    """
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
