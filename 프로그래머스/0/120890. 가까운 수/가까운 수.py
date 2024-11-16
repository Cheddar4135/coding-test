def solution(array, n):
    """
    1. 주어진 배열을 정렬한다.
    2. for in array: 정렬된 배열에서 n이 삽입될 왼쪽 원소와 오른쪽 원소를 구한다.
    3. if 둘 중 하나만 존재한다면, 그 원소를 그대로 return
    4. else, 둘 중 더 가가운 원소 return
    * n과 근처 원소값이 일치할 때 => 그냥 바로 n리턴
    * n 삽입 위치가 맨 뒤나 맨 앞일때 예외처리... 
    
    오, 쉬운 방법이 있을 것 같다. 굳이 정렬안해도 될 것 같아.
    1. array의 각 원소에서 n을 뺀다. 
    2. 절댓값 비교해서 가장 작은 놈. 여러개 일때 더 작은 수 구해야하니까 걍 미리 정렬하자.
    """
    array.sort()
    tmp= [abs(i-n) for i in array]
    index = tmp.index(min(tmp))
    return array[index]