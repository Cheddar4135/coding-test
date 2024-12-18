def solution(my_str, n):
    """문자열 인덱싱하면 되겠군
    리스트 원소의 개수: 문자열길이//n + 1 (if 나머지 있다면)"""
    
    if len(my_str)%n:
        items = len(my_str)//n + 1
    else:
        items = len(my_str)//n
    print(items)
    ans = []
    for i in range(items): 
        ans.append(my_str[i*n:(i+1)*n])    
    return ans

def solution(my_str,n):
    ans = []
    for i in range(0,len(my_str),n): #n=3이라면 0,3,6,..
        ans.append(my_str[i:i+n])
    return ans
