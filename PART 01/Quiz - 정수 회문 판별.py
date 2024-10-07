"""
입력받은 정수를 string으로 변환하지 않고 회문인지 아닌지 판별해야한다.
"""
def isPalindrome(x:int) -> Bool:
  """정수 회문 판별
    Arguments:
      x (int) : 정수
    Return:
      Bool : 회문이라면 True, 아니라면 False 반환
  """
  """풀이
  1. 정수를 거꾸로 저장한다.
    1234 / 10 = 123 ...4
    123 / 10 = 12 ... 3
    12 / 10 = 1 ... 2
    1 / 10 = 0 ...1
    reversed = 4321

  2. 그 값이 원래 정수와 같다면 True 반환, 아니라면 False 반환

  특이케이스: 정수가 음수일때 -> 무조건 False
  """
