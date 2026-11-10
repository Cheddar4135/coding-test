"""난이도:

> 문제해석
  k개 수 제거했을때 가장 큰 숫자 문자열로 반환하기
> 제한분석
  O(nlogn)까지 가능해보인다.
  완전탐색으로 탐색하긴 어려워보임.
> 풀이전략
  우선순위를 정의하는게 관건이다.
  
  1번예시: 가장 작은 수 1,2가 삭제됨
  2번예시: 가장 작은 1,1,2가 앞에서부터 삭제됨
  3번예시: 가장 작은 1,1,2,2가 삭제되지 않고 앞에서 4,1,2,2 삭제
 
  
  앞에서부터 길이2개의 윈도우를 생각한다.
  앞 숫자를 지우고 새로 이웃이 된 숫자도 다시 비교하려면..
  리스트나 문자열로 하는건 비효율적.
  
  스택으로 return한다고 생각한다.
  4 넣었음. 
  1 넣어
  7 넣기전에 앞에 1 빼. 넣기전에 4 빼.
  7 넣어
  2 넣어
  5 넣기전에 2 빼
  
 
> 알고리즘은? 스택 
 
"""

def solution(number, k):
    stack = []
    cnt = 0 
    number = [int(i) for i in number]
                 
    for i, num in enumerate(number):              
        while stack and stack[-1] < num :
            if cnt == k:
                stack.extend(number[i:])
                return "".join(map(str,stack))
            #print(f"{stack[-1]}을 제거합니다.")
            stack.pop()
            cnt +=1
        stack.append(num)
        
    # k 다 안지웠는데 검사 끝나면
    return "".join(map(str,stack[:len(number)-k]))
