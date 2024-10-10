def solution(slice, n):
    """한 사람당 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지 반환
    slice: 피자 조각 수 (2조각~10조각)
    n : 피자 먹는 사람의 수 (1~100명)
    
    (ans*slice)//n이 최소 1이상이어야함
    """
    ans = 1
    while (slice*ans)//n < 1:
        ans+=1
    return ans