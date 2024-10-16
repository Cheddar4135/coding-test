def solution(angle):
    if 0 < angle and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        print("angle범위가 초과되었습니다.")