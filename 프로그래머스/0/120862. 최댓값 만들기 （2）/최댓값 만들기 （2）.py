def solution(numbers):
    ans = -999999999
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            ans = max(ans, numbers[i]*numbers[j])
            
    return ans


def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-2]*numbers[-1])
