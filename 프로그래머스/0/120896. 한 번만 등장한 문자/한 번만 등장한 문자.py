def solution(s):
    unique = [char for char in s if s.count(char)==1]
    return "".join(sorted(unique))
