"""난이도:
> 문제해석:
  장르별 베스트 2개씩 모아 앨범 출시하기
  
  정렬순서
  1. 재생횟수 많은 장르
  2. 재생횟수 많은 노래 > 고유번호 낮은 노래
  
  
  필요한 딕셔너리
  1. 장르 : 총 재생횟수  {"pop": 1900, "rock": 900}
  2. 장르 : (곡 번호, 재생횟수), (곡 번호, 재생횟수)
  
"""
from collections import defaultdict

def solution(genres, plays):
    g_total_play = defaultdict(int)
    g_songs_info = defaultdict(list)
    
    for idx, g in enumerate(genres):
        g_total_play[g] += plays[idx]
        g_songs_info[g].append((idx, plays[idx]))
        
    results = []
    # 재생횟수 많은 장르부터
    for g in sorted(g_total_play, key = g_total_play.get, reverse=True):
        ranked = sorted(g_songs_info[g], key=lambda song: (-song[1], song[0]))
        results.extend(idx for idx, _ in ranked[:2])
        
    
    return results