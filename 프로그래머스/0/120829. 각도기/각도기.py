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

def solution(angle):
    """코드분석
    angle//90 : 예각이라면 0, 평각이라면 2, 둔각이나 직각은 1
    angle%90 : 평각,직각이라면 0, 둔각이나 예각은 0보다큰 값

    예각 : 0 + 1
    직각: 2 + 0
    둔각: 2 + 1
    평각: 4 + 0
    """
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
