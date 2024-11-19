def solution(cipher, code):
    ans = ""
    while len(cipher)//code:
        ans += cipher[code-1]
        cipher=cipher[code:]
    return ans

def solution(cipher, code):
    return cipher[code-1::code]

def solution(cipher,code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))
