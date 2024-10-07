"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

"""
def search(self, nums: List[int], target: int) -> int:
  """
    Arguments:
      nums(list) : 오름차순 정렬된 정수형 배열
      target(int) : 정수
    Return:
      int : target의 인덱스값을 반환, 없으면 -1

    #binary search #two-pointer
    길이가 N인 일차원 배열에서 특정 값의 인덱스를 찾는 경우 시간 복잡도는 O(N)
    O(logN)의 시간복잡도로 문제를 해결하려면 binary search를 이용하자.
    다만 Binary search의 경우 오름차순으로 정렬된 배열에만 적용이 가능하다.
  """
  
