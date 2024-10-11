def solution(money):
    price = 5500
    return [money//price, money%price]

def solution(money):
    price = 5500
    return list(divmod(money,price))

"""파이썬 내장함수 divmod()를 이용하면 몫과 나머지를 한번에 구할 수 있다.
계산결과를 (몫, 나머지) 튜플로 반환해준다.
"""
