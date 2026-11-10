"""난이도: 상 (시간초과 해결 관건)
> 문제분석
  [1,2,3,4,5], 7 -> 부분수열합이 7 -> [3,4] -> [2,3]
  
> 풀이전략
  그냥 찾으려하면 O(n^2)이상 소요될 수 있음. 투포인터 적용.
  이미 정렬된 걸 이용한다.
  left와 right 모두 시작위치, right는 for문 역할
    - 부분합이 k보다 작아 -> right 늘리기
    - 부분합이 k보다 커 -> left 줄이기
    
> 전략:
  매번 sum 안하게 관리하기
  답후보 모두 저장할 필요 없이 가장 짧은거 기억하면 됨 
  인덱스 에러 조심하기
    
"""

def solution(sequence, k):
    s = sequence
    left = right = 0
    total = s[0]
    
    best_len = len(s) +1
    
    while left <= right and right < len(s):
        
        # right 유지, left 이동 후 다음반복으로 넘어감
        if total > k:
            total -=s[left]
            left +=1
            continue
        
        # 답 후보 갱신 후 right 증가
        elif total == k:
            length = right - left + 1
            if length < best_len:
                best_len = length
                ans = [left,right]
            right += 1
        
        # right 증가
        else:
            right +=1
        
        if right < len(s):
            total += s[right]
        

    return ans