def solution(n):
    """
    순서쌍 (first,last)
    -first를 찾으면 last는 n/first니까 바로 구할 수 있음. O(1)
    -first를 찾는방법
        1. 1~n까지 순회하며 나누어 떨어지는 수를 찾는다. O(n)
        2. 기억안남.
        
    잠깐 어차피 순서쌍의 개수를 구하는 거니까. 그냥 약수찾는 문제네.
    1. 1~n까지 순회하며 나누어 떨어지는 수를 카운트한다.
    """
    cnt = 0
    for i in range(1,n+1):
        if not n%i:
            cnt +=1
    return cnt