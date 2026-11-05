"""난이도: 최상 (복습반드시)
> 후기:
  순열 라이브러리를 쓸 수 있다면 편했겠지만..
  그게 아닌걸 가정하고 풀면 너무 힘들었다. dfs 적인 풀이라는데 솔직히 잘모르겠음.
  지피티의 훈수가 많이 들어갔다. 
  반드시 복습!

> 문제분석:
  len(numbers) <=7밖에 안됨
  즉 최대 7개의 종이조각으로 소수 몇개 만들 수 있는지 파악하기
  7!의 경우의 수->충분히 완전탐색으로 풀 수 있을 것 같음
  다만 저번 dfs 문제의 교훈을 바탕으로 재귀적으로 푸는걸 시도해보자.
  
> 알고리즘선택:
  솔직히 그래프는 전혀 생각나지 않는다. 걍 완전탐색 할 수 밖에..
"""
def solution(numbers):
    
    # 기능1. 입력한 정수가 소수인지 판별
    def isPrime(n : int) -> bool:
        if n == 1 or n == 0:
            return False
        
        for i in range(n//2,1,-1):
            if not n%i:
                return False
            
        return True
    
    # 기능2. 문자열에서 c개의 문자 선별해 만들 수 있는 모든 문자열 반환
    # 재귀설계: 한글자 고르기 + 나머지로 순열 만들기
    # find("1,2,3", 2)
    # "1" &  find("2,3", 1) -> "1" &  ["2","3"] -> ["12","23"]
    # ...
    def findPermu(numbers : str, c : int) -> list[str]:
        permu = []
        # 종료조건: c
        if c == 0:
            return [""]
        
        # 떠넘기기
        for i in range(0, len(numbers)):
            for ns in findPermu(numbers[:i]+numbers[i+1:], c-1):
                permu.append(numbers[i]+ns)
                
        return permu
                         
    # 기능2 Test. 
    #return findPermu("17",2), findPermu("123",3), findPermu("123",1)
    
    # 메인로직
    permu = []
    for c in range(1,len(numbers)+1):
        permu = permu + [int(i) for i in findPermu(numbers,c)]
    permu = list(set(permu))

    print(permu)
    answer=0
    for i in permu:
        if isPrime(int(i)):
            print(f"소수발견!: {i}")
            answer+=1
    return answer