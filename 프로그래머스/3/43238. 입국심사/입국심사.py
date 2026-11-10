""" 난이도:
> 문제이해:
  n 입국심사대기자
  times, len(times) 심사대당 소요시간, 심사대 개수
  return 최소소요시간
  
> 알고리즘선택:
  n이 10억임. 최대한 O(logn)으로 줄이는게 관건임
  이미지를 생각하면 3개의 큐에 프로세스가 들어가는 그림
  문제는 len(n)의 리스트 만들었을때 메모리/시간이 될지? -> X
  직접 해보니까 안된다.
  최대한 수식적으로 계산해서 메모리효율적으로 해야함.
 
> 풀이힌트 from 지피티:
  "n명을 보내는데 몇 분이 걸릴까"를 
  "k분이 주어지면 최대 몇명까지 심사할 수 있을지"로 접근하라.
  사람을 한 명씩 배치하는 대신, 심사대별로 그 숫자를 계산하기
  
  n = k // 7 + k // 10
  6 = 4 + 2
  
  만족시키는 최소 k를 찾아야함.
  탐색하는 k의 순서는? 단순히 1분부터 시작하면 망함
  가장 빠른 심사대 단독으로 했을때 걸리는 시간 이상
  가장 빠른 심사대 len(times)개로 했을때 걸리는 시간 이하임
  이걸 이분 탐색으로 하면 빠른갑다
  6 = k // 7  -> k = 7 * 6 
  6 = k // 7 + k // 7  -> k = 7 * (6/2를 올림)
  올림팁: A/B의 올림 -> (A+B-1)//B
  
  k범위 정해서 해당 k에 처리하는 인원보고 많아 -> k줄여. 적어->k높여.
  k처리인원이 n이 되는 여러개 k가 존재할 것임. 그럼 가장 작은거.
"""

def solution(n, times):
    # 제일 빠른 기기 혼자 일할때
    max_time = min(times) * n
    
    # 모두가 동일한 속도로 일할때
    min_time = min(times) * ((n+len(times)-1) // len(times))
    
    # 이분탐색
    def binary_search(min_time, max_time):        
        if min_time == max_time:
            return min_time
        
        mid = (min_time + max_time) //2
        max_n = sum([mid //t for t in times])
        
        if max_n >= n:
            return binary_search(min_time, mid)
        
        else:
            return binary_search(mid+1, max_time)
            
        
    return binary_search(min_time, max_time)