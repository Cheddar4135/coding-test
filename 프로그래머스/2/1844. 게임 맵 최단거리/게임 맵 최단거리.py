"""난이도: 중상상
> 총평:
  알고리즘 선택 자체는 쉽게 떠오른다. 근데 이제 구현이 힘든... 거의 2시간걸렸다.
> 문제분석:
  maps 크기 자체는 작다. 100*100이 최대임. (r,c)=1이 벽이 없는 자리다
  첫위치+마지막위치 포함해서 칸의 개수를 세야한다. 도착불가능할시 -1
> 알고리즘 선택:
  (r,c)=1끼리 연결이용해서 그래프 구성하고 루트(시작점)부터 특정리프노드(도착점)까지 거리 세기
  최단거리(depth)를 찾아야하기에 bfs가 적합할 듯하다.
> 파이썬 문법:
  deque([(r,c)]) 꼭 튜플을 리스트로 한번 감싸줘야한다. deque((r,c))->deque([r,c])
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
    3. 999 대신 미방문은 -1로, 상하좌우는 방향 배열 사용한 반복문으로
    4. bfs라는 함수는 사실 불필요, 출발지가 (0,0)으로 고정이므로
    """
    n=len(maps)
    m=len(maps[0])

    # -1은 미방문, 시작거리를 1로 함으로써 맨 마지막 수식 간소화
    dist = [[-1]*m for i in range(n)]
    dist[0][0]=1 
    queue=deque([(0,0)])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
    while queue:
        r,c = queue.popleft()
        
        #조기종료: 출발지가 도착지
        if (r,c)==(n-1,m-1):
            return dist[r][c]

        #상하좌우 탐색 (와 훨씬 더 효율적이네!)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <=nr < n and 0 <=nc < m):
                continue
            
            #초기방문이 아니라면 패스
            if maps[nr][nc] == 0 or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            queue.append([nr,nc])
        
    return dist[n-1][m-1] 
        
    
    