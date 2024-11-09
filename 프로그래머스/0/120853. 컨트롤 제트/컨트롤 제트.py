def solution(s):
    slist = s.split(' ')
    ans = 0
    for i,char in enumerate(slist):
        if char=='Z':
            ans-=int(slist[i-1])
        else:
            ans+=int(char)
    return ans

def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()
    return sum(stack)
