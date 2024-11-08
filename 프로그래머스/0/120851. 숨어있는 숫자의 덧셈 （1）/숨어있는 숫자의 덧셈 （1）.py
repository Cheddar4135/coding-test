def solution(my_string):
    sum = 0
    for char in my_string:
        if char.isdigit():
            sum+=int(char)
    return sum