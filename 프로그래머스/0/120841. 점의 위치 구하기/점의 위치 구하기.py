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
