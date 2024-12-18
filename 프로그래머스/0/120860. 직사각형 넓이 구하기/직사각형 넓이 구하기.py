def solution(dots):
    dots
    x = max(abs(dots[1][0]-dots[0][0]),abs(dots[2][0]-dots[1][0]))
    y = max(abs(dots[1][1]-dots[2][1]),abs(dots[1][1]-dots[0][1]))
    return x*y