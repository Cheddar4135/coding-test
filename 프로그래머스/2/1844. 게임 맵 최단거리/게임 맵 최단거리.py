"""난이도: 중상상
> 총평:
  알고리즘 선택 자체는 쉽게 떠오른다. 근데 이제 구현이 힘든... 거의 2시간걸렸다.
> 문제분석:
  maps 크기 자체는 작다. 100*100이 최대임. (r,c)=1이 벽이 없는 자리다
  첫위치+마지막위치 포함해서 칸의 개수를 세야한다. 도착불가능할시 -1
> 알고리즘 선택:
  (r,c)=1끼리 연결이용해서 그래프 구성하고 루트(시작점)부터 특정리프노드(도착점)까지 거리 세기
  최단거리(depth)를 찾아야하기에 bfs가 적합할 듯하다.
"""

from collections import deque

def solution1(maps):
    """풀이1
    1. 맵을 리스트형 그래프로 변환한다.
        maps -> graphs
        graphs=[
          (0,0) -> (1,0)
          (0,2) -> (0,3), (1,2)
          ...
        ]
    2. 다익스트라를 적용한다.
    """
    n = len(maps)
    m = len(maps[0])
    
    
    # 1. (r,c)=1 인 셀에 대해서만 그래프 표현
    graphs = {}
    for r in range(n):
        for c in range(m):
            nxt_cells = []
            if maps[r][c]==1:
                # 상하좌우를 탐색한다.
                if r+1<=n-1: 
                    if maps[r+1][c] : nxt_cells.append((r+1,c)) 
                if c+1<=m-1:
                    if maps[r][c+1] : nxt_cells.append((r,c+1)) 
                if r-1>=0:
                    if maps[r-1][c] : nxt_cells.append((r-1,c)) 
                if c-1>=0:
                    if maps[r][c-1] : nxt_cells.append((r,c-1)) 
                graphs[(r,c)] = nxt_cells
    # print(graphs)
    
    # 2. (0,0)에서 시작해서 (n-1,m-1)까지의 최단 depth 찾기
    # 아 이거 다익스트라로 풀어야하나..?
    
    def dikstra(start):
        # 초기세팅
        dist = [[9999]*m for i in range(n)]
        r,c = start
        # 그냥 deque(start)하면 deque([0,0])이 되버림.
        queue = deque([start])
        dist[r][c] = 0

        # start
        while queue:
            r,c = queue.popleft()
            for nr, nc in graphs[(r,c)]:
                if dist[r][c] + 1 < dist[nr][nc] :
                    dist[nr][nc] = dist[r][c]+1
                    queue.append((nr,nc))
        print(dist)
        return dist
    
    ans = dikstra((0,0))
    ans = ans[n-1][m-1]
    return ans+1 if ans<9999 else -1

def solution(maps):
    """방법1개선
    1. 그래프를 따로 만들지 않고 바로 계산해보자.
    2. 간선이 모두 1이기 때문에 더 짧은 거리인지 비교할 필요가 없다.
    """
    n=len(maps)
    m=len(maps[0])
    
    def bfs(start):
        sr, sc = start
        dist = [[999]*m for i in range(n)]
        dist[sr][sc]=0
        queue=deque([(sr,sc)])
        
        while queue:
            r,c = queue.popleft()
            nxt = []
            if r-1 >=0 and maps[r-1][c] : nxt.append((r-1,c)) #append는 튜플을 하나의 원소로 받음
            if c-1 >=0 and maps[r][c-1] : nxt.append((r,c-1))
            if r+1 <=n-1 and maps[r+1][c] : nxt.append((r+1,c))
            if c+1 <=m-1 and maps[r][c+1] : nxt.append((r,c+1))
            
            for nr, nc in nxt:
                if dist[nr][nc] ==999:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append([nr,nc])
        print(dist)
        return dist
        
    ans = bfs((0,0))[n-1][m-1]
    
    return ans+1 if ans <999 else -1
        
    
    