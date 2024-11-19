def solution(my_string, num1, num2):
    """
    문자열로는 item 할당이 안되니까, 리스트로 바꾸고 swap을 진행한다.
    """
    my_list = list(my_string)
    my_list[num1],my_list[num2]=my_list[num2],my_list[num1]
    return ''.join(my_list)