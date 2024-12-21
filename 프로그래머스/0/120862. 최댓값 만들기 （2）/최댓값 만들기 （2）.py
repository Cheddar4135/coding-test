def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    t1 = max(numbers)
    numbers.remove(t1)
    t2 = max(numbers)
    
    t3 = min(numbers)
    numbers.remove(t3)
    t4 = min(numbers)
    return max(t1*t2, t3*t4)