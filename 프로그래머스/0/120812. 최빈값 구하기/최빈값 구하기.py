def solution(array):
    """딕셔너리를 이용한 풀이
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

def solution(array):
    """count를 활용한 다른 사람의 풀이
    list의 count함수는 특정 원소가 list에 몇개 있는지 반환한다.
    문제의 array길이는 1000개로 제한되어있다.
 
    array : [1,1,2,2,2,3,3,3,3]
    idx : [0,2,3,4,0,0,0,0,0,0,,0,0,0,0,0,0,0,0,0,0,0,...]
    idx.count(4) = 1 -> return 3
    
    워우..이해하기도 힘드네.. 어떻게 한거지.
    함수하나 또 배웠다. list.index(4) : 4라는 원소의 인덱스를 반환
    """
    idx = [0] * 1001
    for i in array:
        idx[i] +=1
    if idx.count(max(idx)) >1:
        return -1
    return idx.index(max(idx))

from collections import Counter
def solution(array):
    """counter를 이용한 풀이
    Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
    >>> Counter({'hi': 3, 'hey': 2, 'hello': 1}) 
    Counter("hello")
    >>> Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1}) 카운터객체 반환한다
    Counter 클래스는 딕셔너리를 확장하고 있기 때문에, 딕셔너리에서 제공하는 API를 그대로 다 사용가능
    아, 내가 딕셔너리로 한 짓을 Counter로 쉽게 할 수 있구나.
    """
    a = Count(array).most_common(2)
    if len(a) == 1: #예외처리: array의 원소가 다 같은 수였을때 혹은 하나였을때의 경우 list out of range 방지
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
    
