#그냥 반복문 쓰는 것보다 시간 복잡도 절약 가능
def solution(s1, s2):
    dict = {i:1 for i in s1}
    answer = sum(1 for j in s2 if j in dict) 
    return answer
