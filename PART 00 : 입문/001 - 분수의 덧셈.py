"""
[프로그래머스] 코딩테스트 입문 > 분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808
"""

"""배운점: 거꾸로 반복 for문 돌리는 방법
for i in range(10,1,-1)
  print(i)
이런식으로 꼭 range()에 -1인자를 추가로 넣어줘야한다.
그냥 range(10,1)하면 반복문 자체가 실행이 안됨.
"""
def solution(numer1, denom1, numer2, denom2):
    """ 분수의 덧셈
    numer : 덧셈 결과의 분자 
    denom : 덧셈 결과의 분모 
    
    기약분수로 반환하기 위해 numer과 denom의 최대공약수로 각 수를 나눠야 한다. 
    최대공약수는 어떻게 구하지? 
    공약수 : 둘다 나눴을 때 나머지가 0이되는 수.
    공약수 범위는 2~(둘 중 작은 값)
    최대공약수 구하면 장땡이니까 range를 큰값부터 역으로 돌리는게 낫겠군.
    """
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 * denom2
    
    small = min(numer, denom)
    divisor = 1
    for i in range(small, 1,-1):
        #print(f"{numer}과 {denom}의 약수찾기:{i}")
        if (numer % i == 0) and (denom % i == 0):
            #print(f"{i}는 최대공약수입니다.")
            divisor = i
            break
    numer/=divisor
    denom/=divisor
    return [numer, denom]
