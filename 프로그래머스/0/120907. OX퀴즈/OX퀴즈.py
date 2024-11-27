def solution(quiz):
    answer=[]
    for q in quiz:
        answer.append(isright(q))
    return answer

def isright(mystr): #"3 - 4 = -3"
    left, right = mystr.split(' = ')
    #left = left.replace(' - ',' + -').split(' + ') #3 + -4 => 3,-4=
    if eval(left) == int(right):
        return "O"
    else:
        return "X"
    
# 반례: -3 + 1, -4 - 5 등의 경우 => 잘 동작함
# 뭐가 문제지? -3 - -2 이런 경우 => -3,--2로 split되어서 int변환시에러남.
# 사용자의 수식의 입력에 따라 에러 발생 위험성이 큰 코드임. 파이썬 내장함수 eval을 사용하는게 안전함.
    