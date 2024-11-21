def solution(my_string):
    my_list = my_string.split(' ')
    ans=int(my_list[0])
    for i,item in enumerate(my_list):
        if item == "+":
            ans+=int(my_list[i+1])
        elif item == "-":
            ans-=int(my_list[i+1])
    return ans


"""
발전 : 연산자는 무조건 짝수번째 요소에 있으니까 꼭 리스트의 모든 요소를 순회할 필요가 없다.
"""
def solution(my_string):
    my_list = my_string.split(' ')
    ans=int(my_list[0])
    for i in range(1,len(my_list),2):
        if item == "+":
            ans+=int(my_list[i+1])
        elif item == "-":
            ans-=int(my_list[i+1])
    return ans


"""
프로그래머스 1등 풀이
1. replace(' - ',' + -' ) "3 + 4 + 5 - 5" => "3 + 4 + 5 + -5" 
2. split(' + ')하고 각 요소 정수화해서
"""
def solution(my_string):
    return sum([int(i) for i in my_string.replace(' - ',' + -').split(' + ')])
