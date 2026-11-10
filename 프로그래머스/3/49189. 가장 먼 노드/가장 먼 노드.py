"""
> 문제이해
  n개의 노드
  1번노드에서 가장 멀리 떨어진 노드, 즉 최단경로 이동시 통과하는 간선개수많은
  양방향 간선이다.
"""

from collections import deque, defaultdict

def makegraph(edge):
    graph=defaultdict(list)
    for n1,n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph
    
def solution(n, edge):
    q = deque()
    dist = [50001]*(n+1)
    
    # state = (노드번호, 통과간선개수)
    q.append(1)
    dist[1] = 0

    graph = makegraph(edge)
    while q:
        node= q.popleft()
        for nxt in graph[node]:
            if dist[node]+1 < dist[nxt]:
                q.append(nxt)
                dist[nxt] = dist[node]+1
    
    dist.remove(50001)
    return dist.count(max(dist))