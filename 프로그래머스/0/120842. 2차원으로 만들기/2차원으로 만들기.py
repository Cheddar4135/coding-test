import numpy as np
def solution(num_list, n):
    a = np.array(num_list)
    return a.reshape(-1,n).tolist()