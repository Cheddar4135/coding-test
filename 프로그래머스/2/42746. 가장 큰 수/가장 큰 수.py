def solution(numbers):
    """ 
    > 난이도: 중하
    벼락치기 해야해서 지피티 도움받음
    혼자할땐 끝자리연장전략(89 -> (8,9,9,0)으로 했는데 
    특정 케이스에서 문제 있었음
    또 원소가 0개거나 0으로 시작할때 전처리도 중요했음
    
    테스트케이스 많이 생각하는것의 중요성 느끼게해줌
    
    cmp_to_keys하면 편하다는데 굳이 배우고 싶지 않았음
    """
 
    def make_key(s): #num=789
        return s* (12//len(s))
    
    rank = sorted(map(str, numbers), key = make_key, reverse=True)
    
    # 0으로 시작하는거 제거, 빈문자열 되면 "0"반환            
    return "".join(map(str,rank)).lstrip("0") or "0"