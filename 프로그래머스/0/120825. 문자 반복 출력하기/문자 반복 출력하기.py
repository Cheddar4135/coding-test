def solution(my_string, n):
    answer=""
    for char in my_string:
        answer+=char*n
    return answer

def solution(my_string,n):
    return ''.join(char*n for char in my_string)
