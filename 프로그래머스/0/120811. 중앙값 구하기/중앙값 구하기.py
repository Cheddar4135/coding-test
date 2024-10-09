def solution(array):
    """배열의 중앙값을 리턴하는 함수
    array (list) = 길이가 홀수인 정수 배열
    
    1. 파이썬 메서드를 이용해 배열을 정렬한다.
      -list.sort()
        list.sort() : 리스트를 오름차순으로 정렬
        list.sort(reverse=True) : 리스트를 내림차순으로 정렬
        sort()는 해당 list 원본을 바꾼다. 
      -sorted(list)
        cp = sorted(list, reverse=True) : 리스트 내림차순 정렬
        정렬된 복사본을 생성한다.
              
    2. (배열의 길이)//2 번째 인덱스의 값을 반환한다.
    
    """
    array.sort()
    return array[len(array)//2]