def solution(numbers):
    """
    리스트의 가장 큰 두 수의 곱을 구하는 함수
    
    main idea1
    1. numbers의 가장 큰 원소를 찾는다.
    2. numbers에서 가장 큰 원소를 제거한다.
    3. numbers의 가장 큰 원소를 찾는다.
    
    main idea2
    1. numbers를 내림차순으로 sorting한다.
    2. 맨 처음 두 원소를 가져오고 곱한다.

    """
    max1 = 0
    for num in numbers:
        if num > max1:
            max1 = num
            
    numbers.remove(max1)
    
    max2 = 0
    for num in numbers:
        if num > max2:
            max2 = num
            
    return max1*max2