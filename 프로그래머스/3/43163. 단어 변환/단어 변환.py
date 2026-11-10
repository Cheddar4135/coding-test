"""난이도:
> 문제이해:
  begin: hit, target = cog
  hit -> hot -> dot -> dog -> cog

> 풀이전략:
  한개의 알파벳만 다른걸로만 이동 가능하니까
  후보군 추리는 함수 필요하겠군. 
  start부터 target까지 모든 경로를 찾을 이유는 없다.
  최단거리로 도달하는걸 찾으면 되므로 bfs가 적절하다.
  
  (후보를 끝까지 만들어야 판정할 수 있거나, 중간에 틀린 갈래를 잘라낼 수 있는 문제라면 DFS로 한 갈래씩 탐색하기 편하다)
  
"""
from collections import deque

def solution(begin, target, words):    
    
    # 보조함수. 한개의 알파벳만 다른 후보군을 반환한다.
    def findnexts(begin):
        candi = []
        for word in words:
            cnt = 0
            for i,w in enumerate(word):
                if w != begin[i]:
                    cnt +=1
            if cnt == 1:
                candi.append(word)
        return candi
    
    # BFS: 목표 begin->target 최단경로, 변환불가시 0 
    # state = (curr, steps)
    q = deque([(begin, 0)])
    visited = {begin}
    
    while q:
        curr, steps = q.popleft()
        if curr == target:
            return steps
        
        for nxt in findnexts(curr):
            if nxt in visited:
                continue
            q.append((nxt,steps+1))
            visited.add(nxt)
            
        
    return 0
                
            
    
    
