def solution(numbers, k):
    answer = []
    for i in range(k):
        answer.append(numbers)
    answer = sum(answer, [])
    return answer[(k-1)*2]

def solution(numbers, k):
    return numbers[(k-1)*2*len(numbers)]
