"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
"""함수 설명
    Arguments:
        target (int): 자연수
        nums (list): 자연수로 구성된 리스트
- 합이 타깃 이상인 부분배열의 최소 길이를 반환한다.
- 조건 충족하는 부분배열이 없다면, 0을 반환한다.
- (주의)부분배열 : 주어진 배열에서 끊기지 않고 인접한 원소들의 집합
[1,2,3,4,5]의 부분배열로 [1,3,5]는 될 수 없다.
"""    
"""알고리즘 #Binary Search #two pointer #log(n)
1. sum이 target보다 작다면=>뒤쪽포인터 한칸 뒤로 이동
2. sum - 앞쪽포인터값이 target보다 크면 => 앞쪽 포인터 이동
음 근데 이러면 완전한 탐색이 안될거같은디..아 졸려 모르겠다. 내일 다시 해보자.
"""
"""수도코드

"""
