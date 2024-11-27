def solution(str1, str2):
    return 2 if str1.replace(str2,"")==str1 else 1

def solution(str1, str2):
    return 1 if str2 in str1 else 2

def solution(str1,str2):
    return 1 + int(str2 not in str1)
