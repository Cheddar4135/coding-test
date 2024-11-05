def solution(n):
    """
    n이하의 합성수의 개수 찾기
    
    1. n이 합성수인지 아닌지 판별할 것
        - 1부터 n까지 순회하면서 나누어떨어지는 횟수가 3번이상이면 합성수
    2. n = n-1로 업데이트하면서 반복 (n=1일때까지)
    3. 합성 수의 개수 반환
    
    main idea
        2의 배수는 합성수임
        3의 배수는 합성수임
        5의 배수는 합성수임
        ...
        
    """
    def isComposite(n):
        for i in range(2,n):
            if not n%i:
                print(f"{n}은 합성수")
                return True
        return False
    
    sum = 0
    for num in range(1,n+1):
        sum+=int(isComposite(num))
    return sum