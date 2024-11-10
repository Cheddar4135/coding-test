"""
main idea: 리스트로 바꿔서 set함수로 중복제거 후 다시 문자열로 반환
--> 문제점: set으로 하면 순서가 뒤죽박죽이 된다. 2번째로 중복해서 나온문자를 제거해야한다.

main idea: 문자열 왼쪽부터 오른쪽으로 순회하면서 해당 문자가 이미 나온 문자라면 제거
    1. for c in my_string: 
    2. 처음 나온 문자라면 dic[c] = 1, ans+=c
    3. 만약 두번째 나온 문자라면, skip
"""
# using string 'in' keyword: 조회에 O(n) 소요
def solution(my_string):
    ans = ''
    for c in my_string:
        if c not in ans:
            ans+=item
    return ans

# using dictionary key 'in' keyword: 조회에 O(1)사용
def solution(my_string):
    ans = ''
    dic = {}
    for c in my_string:
        if c not in dic:
            dic[c] =1
            ans+=c
    return ans
