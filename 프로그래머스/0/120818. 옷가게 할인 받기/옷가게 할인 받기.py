def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    else:
        return price

#딕셔너리 이용한 다른사람의 신박한 풀이. 확실히 이러면 코드 확장성이 좋겠군.
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
