def solution(numbers, direction):
    """
    main idea
        인덱스 슬라이스 기능을 이용하면 간단히 풀 수 있다.
    주의
        [:end] 처음부터 end-1 인덱스까지
        [start : end : step] step만큼 문자를 건너뛰면서 추출
    """
    if direction=="right":
        new = [numbers[-1]] + numbers[:-1]
    elif direction=="left":
        new = numbers[1:]+ [numbers[0]]
    return new 
