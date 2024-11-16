def solution(order):
    dic369={3:1,6:1,9:1} #key 조회는 O(1)이니까 
    ans = 0
    while order:
        if order%10 in dic369:
            ans+=1
        order//=10
    return ans

def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer
