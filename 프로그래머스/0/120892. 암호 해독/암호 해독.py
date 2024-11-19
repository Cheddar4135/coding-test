def solution(cipher, code):
    ans = ""
    while len(cipher)//code:
        ans += cipher[code-1]
        cipher=cipher[code:]
    return ans