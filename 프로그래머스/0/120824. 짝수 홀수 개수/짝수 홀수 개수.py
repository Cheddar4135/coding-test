def solution(num_list):
    even = 0; odd = 0
    for num in num_list:
        if num %2==0:
            even+=1
        else:
            odd+=1
    return [even, odd]

def solution(num_list):
    """나머지를 인덱스로 활용한 센스있는 풀이
    """
    answer = [0,0] #짝수, 홀수 순으로 반환해야함
    for num in num_list:
        answer[num%2]+=1
    return answer

    """만약 홀수, 짝수 순으로 반환해야했다면
    """
    answer = [0,0] #홀수, 짝수 순으로 반환
    for num in num_list:
        answer[(num+1)%2]+=1
    return answer
