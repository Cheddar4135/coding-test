"""
> 문제분석:
  직사각형격자 maps n,m <=100, 통로만 통과가능. 미로탈출문 레버당기기필요
  S 시작지점은 (0,0)고정이 아님, E 출구 역시 마찬가지
  역시 다익스트라 해야겠는데..? (S->L최단 + L->E최단)
"""
from collections import deque

def solution(maps):
    # 1. 지도 전처리
    n = len(maps); m=len(maps[0])
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] == "S":
                start = (r,c)
            elif maps[r][c] =="L":
                lever = (r,c)
            elif maps[r][c] == "E":
                end = (r,c)
                
    print(f"start:{start}, lever:{lever}, end:{end}")
    
    # 2. 다익스트라 정의: 출발지 2곳이라 함수 필요
    def dijkstra(start,end):
        sr, sc = start
        er, ec = end
        dist=[[-1]*m for i in range(n)]
        queue=deque([(sr,sc)])
        dist[sr][sc]=0 
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        
        while queue:
            r,c = queue.popleft()
            for (dr, dc) in directions:
                nr = r + dr ; nc = c + dc
                if (0 <= nr and nr < n) and (0 <= nc and nc < m):
                    if maps[nr][nc] != "X" and dist[nr][nc] == -1:
                        dist[nr][nc]=dist[r][c]+1
                        # queue.append([(nr,nc)])했다가 ValueError: not enough values to unpack (expected 2, got 1) 계속 떴음;;하
                        queue.append((nr,nc))

        return dist[er][ec]

    a=dijkstra(start, lever)
    b=dijkstra(lever, end)
    
    if a == -1 or b ==-1:
        return -1
    else:
        return a + b