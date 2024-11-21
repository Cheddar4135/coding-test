def solution(my_string):
    my_list = my_string.split(' ')
    ans=int(my_list[0])
    for i,item in enumerate(my_list):
        if item == "+":
            ans+=int(my_list[i+1])
        elif item == "-":
            ans-=int(my_list[i+1])
    return ans
