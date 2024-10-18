def solution(hp):
    """
    이 코드는 개미군단이 언제나 사냥감의 체력에 딱 맞는 병력을 데리고 나갈 수 있다는 가정,
    즉 일개미의 공격력이 늘 1이라는 가정하에만 정답을 내놓을 수있다.
    """
    attack = {'장군개미':5, '병정개미':3,'일개미':1}
    num1 = hp//attack['장군개미']
    num2 = (hp%attack['장군개미'])//attack['병정개미']
    num3 = (hp%attack['장군개미'])%attack['병정개미']
    
    return num1+num2+num3