def solution(my_string, letter):
    return ''.join(my_string.split(letter))

def solution(my_string, letter):
    return ''.join(c for c in my_string if c != letter)

def solution(my_string, letter):
    return my_string.replace(letter, '')
