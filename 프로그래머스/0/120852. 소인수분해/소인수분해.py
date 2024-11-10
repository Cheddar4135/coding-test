def solution(n):
    ans = []
    k = 2
    while n>1:
        if n%k==0:
            ans.append(k)
            n//=k
        elif k >int(n**0.5):
            ans.append(n)
            break
        else:
            k+=1
    return sorted(list(set(ans)))
    
