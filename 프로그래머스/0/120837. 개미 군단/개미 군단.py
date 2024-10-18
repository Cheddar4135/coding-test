def solution(hp):
    """공격력 수정 용이성이 좋은 코드
    이 코드는 개미군단이 언제나 사냥감의 체력에 딱 맞는 병력을 데리고 나갈 수 있다는 가정,
    즉 일개미의 공격력이 늘 1이라는 가정하에만 정답을 내놓을 수있다.
    """
    attack = {'장군개미':5, '병정개미':3,'일개미':1}
    num1 = hp//attack['장군개미']
    num2 = (hp%attack['장군개미'])//attack['병정개미']
    num3 = (hp%attack['장군개미'])%attack['병정개미']
    
    return num1+num2+num3

def solution(hp):
    """간단히 하면 그냥 이 코드
    """
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

def solution(hp):
    """이게 best 방법인듯, 수정용이성도 좋고 코드도 간단하고
    """
    answer = 0
    for ant in [5,3,1]:
        count,hp = divmode(hp,ant)
        answer+=count
    return answer
