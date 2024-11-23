def solution(num, k):
    #num 각자리 수 접근 쉽게 문자열로 바꾸기
    num = str(num)
    #인덱스값 리턴이므로 딕셔너리 조회보다는 그냥 for문
    for i in range(len(num)):
        if int(num[i]) == k:
            return i+1
    return -1