def solution(array):
    """7검사기: 각 원소마다 자리수에 7이 있는지 확인해서 count해야한다
    문자열로 하는게 쉽겠군.."""
    count = 0
    for item in array:
        for c in str(item):
            if c == '7':
                count+=1
        
    return count