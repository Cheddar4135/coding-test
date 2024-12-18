def solution(array):
    """7검사기: 각 원소마다 자리수에 7이 있는지 확인해서 count해야한다
    문자열로 하는게 쉽겠군.."""
    count = 0
    for item in array:
        for c in str(item):
            if c == '7':
                count+=1
        
    return count



def solution(array):
    #그냥 "[2,7,5,77]"로 리스트 자체를 문자열로 바꿔서 7의 개수를 세는 방법도 있다.
    return str(array).count('7')
    
