def solution(array):
    """최빈값 구하기
    array : 정수 배열
    answer : 최빈값 return, 최빈값 여러개일시 -1 return
    
    딕셔너리가 편하겠네 {(특정 원소의 값) : (등장 횟수)}
    
    빈딕셔너리 생성하고, array의 모든 원소에 접근한다.
    만약 해당 원소가 key에 없다면 count['원소'] = 1
    이미 있다면 count['원소']+=1
    
    {1:1, 2:1, 3:3, 4:1}
    키는 [1,2,3,4] - value는 [1,1,3,4]
    value가 가장 큰 값일때의 키를 구한다.
    만약 복수라면 -1리턴
    """
    count = {}
    for item in array:
        if item in count:
            count[item]+=1
        else:
            count[item]=1
    keys = list(count.keys())
    values = list(count.values())
    
    m = max(values)
    max_index = [i for i,val in enumerate(values) if val==m]
    
    if len(max_index) > 1:
        return -1
    else:
        return keys[max_index[0]]
            