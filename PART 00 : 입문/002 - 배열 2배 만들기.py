"""
[프로그래머스] 코딩테스트 입문 > 배열 2배 만들기

여러 방법 중 효율적인 걸 분석해보자.
"""
""" 
배운점 01: numpy배열을 리스트로 변환시키기
  a = np.array([1,2,3])
  a.tolist()
배운점 02: list comprehension
  [표현식 for 항목 in 반복가능객체 if 조건문]

배운점 03: 람다(lambda)
함수를 딱 한 줄만으로 만들게 해주는 훌륭한 녀석
def hap(x, y):
	return x + y
이 함수를 간결하게 (lambda x,y: x + y)(10, 20)로 표현할 수 있다. 
근데 이러면 함수가 이름조차도 없는데 어떻게 사용하는걸까?

map(함수, 리스트)을 이용한다.
리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아준다.
list(map((lambda x: x**2, range(5)))) 이런식으로!
"""
#-방법1: numpy배열 스칼라연산 이용하기---------------
import numpy as np
def dublingArray(numbers):
    nb = np.array(numbers)*2
    return nb.tolist()
# 대략 0.02ms ~ 0.10 ms 소요

#-방법2: 단순 for문----------------------------------
def dublingArray(numbers):
  return [num*2 for num in numbers]
# 대략 0.00ms ~ 0.10 ms 소요. 비슷하게 걸리네

#-방법3: lambda--------------------------------------
ans = list(map(lambda x: x * 2, numbers))
