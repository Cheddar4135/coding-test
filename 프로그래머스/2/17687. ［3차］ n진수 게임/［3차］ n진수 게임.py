"""
> 문제분석:
  m명이면 0~m-1번째까지 수가 사용된다.
  예시: 2진수 4개 2명 1번째로 -> 0,1,10,11,100,101,...
  예시: 16진수 16개 2명 1번째로 -> 0,.,2,.,4,.,6...E, 10, 11, 
  
> 풀이전략:
  1. 진수마다 0~부터 숫자나열리스트. 어디까지? 최대 m * t 개까지 뭐 대충그정도
  2. 그다음 리스트 인덱싱으로 튜브가 말해야하는 숫자 고르기. 간격은 m 간격으로..
  
  리스트보다는 문자열이 좋을듯
  진수마다 나열 어캐함. 라이브러리 없나
"""
def solution(n, t, m, p):
    # 입력: n진수로 0부터 k-1개까지 나열
    # eg. numberchange(10, 5) -> [0,1,2,3,4] -> "01234"
    # eg. numberchange(2,8) -> [0,1,10,11,...] -> "011011..."
    
    def decimaltonum(i,n):
    #     # 테스트용 임의설계-특정진수들만
    #     if n == 10:
    #         return i
    #     if n == 2:
    #         return bin(i)[2:]
    #     if n == 8:
    #         return oct(i)[2:]
    #     if n == 16:
    #         return hex(i)[2:]
        # 전체 동작 성공, 이제 모든 진수로 확장하기
        candidate_digits = ['0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f']
        
        digits = candidate_digits[:n]
        
        if i < n:
            return digits[i]
        
        stack = []
        dividend = i 
        while dividend:
            share = dividend // n
            remainder = dividend % n
            stack.append(digits[remainder])
            dividend = share
        return ''.join(stack[::-1])
            
            
            
        
    def numberschange(n, k):
        numbers=[]
        for i in range(k): 
            num = decimaltonum(i,n)
            numbers.append(num)
        tostring = ''.join(numbers).upper()
        # print(f"{n}진수로 표현한 0~k-1 숫자리스트: {numbers}")
        return tostring

    numbers = numberschange(n,m*t)
    
    # 숫자구하기 
    #  eg. "011011" & t=4, m=2, p=1 -> "0111"
    answer = ""
    for i in range(p-1, len(numbers), m):
        if len(answer) == t:
            break
        answer = answer+numbers[i]
        
    return answer
    
    
    return 1