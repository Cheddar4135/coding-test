def solution(n):
    """
    test case:
        for 12,
        12%2=0 소인수:2 n=6
        6%2=0 소인수:2 n=3
        3%3=0 소인수:3 n=1
        
        for 17,
        17%17=0 소인수:17 n=1
        
        for 27,
        27%3 =0 소인수: 3 n=9
        9%3 = 0 소인수: 3 n=3
        3%3 = 0 소인수: 3 n=1
        
    어떻게 구현할까?
        1. 나눠지는 수 : for i in range(2,int(n**0.5)+1), 
            다 돌아도 없다는 건 해당 n이 소수라는 것(base case)
        2. 만약 n%i==0인 i를 찾았다면, 해당 i는 소인수이고 다시 n대신 n//i넣어 반복
        3. 결과는 중복없이, 오름차순으로 반환
    """
    def factorization(n,factor):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                factor.append(i)
                return factorization(n//i,factor) 
        factor.append(n)
        return 1 #걍 호출 중단 목적일뿐 값은 안중요
    factor=[]
    factorization(n,factor)
    return sorted(list(set(factor)))
    
