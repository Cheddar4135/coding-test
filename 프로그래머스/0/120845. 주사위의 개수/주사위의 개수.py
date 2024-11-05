def solution(box, n):
    """
    > 함수 정보:
        box : [가로길이, 세로길이,높이길이]
        n : 주사위 모서리 길이
        return (int): 상자에 들어갈 수 있는 주사위 최대 개수
        
    > main idea: 박스의 각 모서리의 길이를 주사위 모서리 길이로 나눈 몫만큼 들어갈 수 있다.
    """
    sum = 1
    box = [(boxlen//n) for boxlen in box]
    for i in box:
        sum*=i
    return sum

def solution(box,n):
    x,y,z = box
    return (x//n) * (y//n) * (z//n)

def solution(box,n):
    ans = 1
    for b in box:
        ans *= b//n
    return ans
