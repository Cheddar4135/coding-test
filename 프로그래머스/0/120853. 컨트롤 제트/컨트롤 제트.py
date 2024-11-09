def solution(s):
    slist = s.split(' ')
    print(slist)
    ans = 0
    for i,char in enumerate(slist):
        if char=='Z':
            ans-=int(slist[i-1])
        else:
            ans+=int(char)
    return ans