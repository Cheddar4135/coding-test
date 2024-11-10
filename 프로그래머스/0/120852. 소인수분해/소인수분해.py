def solution(n):
    ans = []
    while n>1:
        for k in range(2,n+1):
            if n%k==0:
                ans.append(k)
                n//=k
                break
    return sorted(list(set(ans)))
    
