def solution(array, height):
    taller=0
    for item in array:
        if item > height:
            taller+=1
    return taller

def solution(array, height):
    return len([i for i in array if i > height])
