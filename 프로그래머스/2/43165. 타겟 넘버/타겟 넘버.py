"""난이도: 상 (복습필수!!)
> 핵심 인사이트:
- 숫자마다 + 또는 -를 선택하므로 전체 경우의 수는 2^N이다.
- 이 선택 과정을 이진트리로 생각할 수 있다. 이때 트리 전체를 만들어 저장하지 않아도, 현재 위치와 누적 합만으로 다음 상태를 탐색할 수 있다.
- 경로 자체가 필요하지 않고, 합만 필요하다는 점을 이용해 더 메모리 효율적으로 풀 수 있다. 

> 어려웠던 점:
- 선택 과정을 트리로 떠올렸지만 어떻게 트리를 리스트로 표현할지, 재귀 코드로 탐색해야하는지 어려웠다.
- 재귀함수가 무엇을 입력받고 무엇을 반환할지 정하는 것이 중요했다.
"""

""" 방법1: 반복문을 이용한 완전탐색
> 알고리즘 선택 근거:
 len(numbers)<=20이므로 총 가능한 경우의 수는 2^20 즉 10^6 정도라 O(n)으로 풀면 1초
> 풀이 전략: 
 1_1 : 모든 경로 다 기억하기 
 1_2 : 합만 기억하기
"""

def solution1_1(numbers, target):
    """
    routes = 
        [[4],[-4]]
        [[4,2],[4,-2],[-4,2],[-4,-2]]
        ...
    """
    routes = [[]]
    
    for n in numbers:
        nxt_routes = []
        for route in routes:
            # 아래코드로 하면 route.append(+n)이 반환하는건 None이라 에러발생
            # nxt_routes.append(route.append(+n))
            # nxt_routes.append(route.append(-n))
            nxt_routes.append(route + [+n])
            nxt_routes.append(route + [-n])
        routes=nxt_routes
    answer = 0
    for route in routes:
        if sum(route) == target:
            print(route)
            answer +=1 
    
    return answer
        
def solution1_2(numbers, target):
    """
    totals = 
        [[4],[-4]]
        [[4+2=6],[4-2=2],[-4+2=-2],[-4-2=-6]]
        ...
        ...
    """
    totals = [0]
    for n in numbers:
        tmp=[]
        for total in totals:
            tmp.append(total + n)
            tmp.append(total - n)
        totals=tmp
        print(totals)
    
    return totals.count(target)

""" 방법2: 재귀를 이용한 DFS 완전탐색
> 알고리즘 선택 근거:
 음 솔직히 그래프문제유형인걸 알고 접근해서 DFS를 떠올렸지 아니면 떠올리기 힘들었을듯
> 풀이 전략: 
 2_1 : 경로도 출력하기. 정답 경로를 공유 리스트 ans에 모은다.
 2_2 : 개수만 출력하기. 각 호출이 가능한 정답 개수를 반환하고, 부모가 두 값을 더한다.
"""

def solution2_1(numbers, target):
    numbers = [0] + numbers
    
    # input: 현재 몇번째 숫자인지, 지금까지 경로는 뭐였는지
    def recur(depth, route, ans):
        # 종료조건: 마지막 숫자가 되면 지금까지경로합이 target이 되는지 확인
        if depth >=len(numbers)-1:
            if sum(route)==target: 
                ans.append(route) 
            return 
        
        # 떠넘기기: 다음차례숫자, 지금까지경로, 지금자기 정답
        recur(depth+1, route + [numbers[depth+1]], ans)
        recur(depth+1, route + [-numbers[depth+1]], ans)
        return ans
    
    paths = recur(0, [], [])
    print(paths)
    return len(paths)

def solution(numbers, target):
    numbers = [0] + numbers
    # input: 현재 몇번째 숫자인지, 지금까지 합은 뭔지
    def recur(depth, total):
        # 종료조건: leaf 노드가 되면 깊이합이 target과 같은지 확인 후 기록
        if depth >= len(numbers)-1 :
            return 1 if target==total else 0 
        
        # 떠넘기기 : 다음차례숫자, 다음차례까지의 합
        return recur(depth+1, total + numbers[depth+1]) + recur(depth+1, total - numbers[depth+1])
        
    return recur(0, 0)
    
    
    

