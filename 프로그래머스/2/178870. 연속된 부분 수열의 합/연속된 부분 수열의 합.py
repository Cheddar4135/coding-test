"""
> 문제분석
  [1,2,3,4,5], 7 -> 부분수열합이 7 -> [3,4] -> [2,3]
  
> 풀이전략
  그냥 찾으려하면 O(n^2)이상 소요될 수 있음. 투포인터 적용.
  이미 정렬된 걸 이용한다.
  left와 right 모두 시작위치, right는 for문 역할
    - 부분합이 k보다 작아 -> right 늘리기
    - 부분합이 k보다 커 -> left 줄이기
"""

def solution(sequence, k):
    s = sequence
    left = right = 0
    total = s[0]
    
    best_len = len(s) +1
    
    while left <= right and right < len(s):
        if total > k:
            total -=s[left]
            left +=1
            continue
        
        if total == k:
            length = right - left + 1
            if length < best_len:
                best_len = length
                ans = [left,right]
        right += 1
        if right < len(s):
            total += s[right]
        

    return ans