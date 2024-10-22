def solution(dot):
    """직관적인 풀이
    """
    if dot[0]> 0 and dot[1]>0:
        return 1
    elif dot[0]<0 and dot[1]>0:
        return 2
    elif dot[0]<0 and dot[1]<0:
        return 3
    elif dot[0]>0 and dot[1]<0:
        return 4
    else:
        print("잘못된 입력")
        return -1

def solution(dot):
    """센스있는 풀이
    x가 양수: 1,4사분면 y가양수:1사분면
    x가 음수: 2,3사분면 y가양수:2사분면
    """
    return [[1, 4], [2, 3]][dot[0] < 0][dot[1] < 0]
