class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        """ 함수 설명
        오름차순으로 정렬된 리스트에 특정숫자를 몇번째에 놓아야 하는지 반환한다.
        Arguments:
            nums (list) : 오름차순 정렬된 정수 리스트
            target (int): 정수
        Return:
            int : target이 삽입되어야할 인덱스 번호
        """
        """특이케이스
        - 리스트 크기가 1일때
        """
        
        # 방법1: 단순 for문 서치-----------------------------------------------------------
        """알고리즘
        target이 리스트를 순회하면서 자기보다 크거나 같은 값을 만나면 해당 인덱스를 반환한다.
        리스트 순회를 끝까지 갔다면 리스트의 마지막 인덱스 뒤의 값을 반환한다.
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

        # 방법2: 이진 탐색-------------------------------------------------------------------
        """알고리즘
        방법1의 런타임복잡도는 O(n)임. O(log n) 런타임 복잡도 갖도록 구현해보자.
        | 두 포인터를 이용한 방법
        - 두 포인터가 리스트 양쪽 끝에서 시작하여, 타깃 값과 두 포인터 가운데의 값을 대소 비교.
        - 타깃 값이 두 포인터 사이에 있도록 유지하며 둘 중 하나의 포인터를 가운데로 이동한다.
        | 슈도코드
        -왼쪽 포인터는 리스트 인덱스(0)에, 오른쪽 포인터는 마지막 인덱스에 위치한다.
        -왼쪽 포인터가 오른쪽 포인터보다 작을 동안, 두 포인터의 중간값 & 타깃 값을 비교한다.
            -만약 타깃이 중간값보다 작다면 오른쪽 포인터를 중간으로 이동한다.
            -만약 타깃이 중간값보다 크다면 왼쪽 포인터를 중간으로 이동한다.
        -반복문을 끝까지 통과하면 (왼쪽과 오른쪽 포인터가 가리키는 값 동일하거나 교차)하면 왼쪽포인터의 인덱스 반환 
        """
        left: int = 0
        right: int = len(nums) -1
        while left <right:
            mid = int((left+right)/2)
            if target < nums(mid):
                left = mid
            if target > nums(mid):
                right = mid
        return nums(left)

        """문제발생
        무한루프를 발생시킨다.
        조건을 (right - left) -1 > 1로 해봐도 무한..
        """
# 방법3: 교수님코드----------------------------------------------------------------------------
    def searchInsert(self, list, value) :
        first = 0
        last = len (list) - 1
        while first <= last:
            mid = (first + last) // 2
            if list[mid]== value:
                return mid
            elif list[mid] < value:
                first = mid + 1
            else:
                last = mid - 1
        return last+1
    """
    Q. 왜 last+1을 리턴해야 하는가? 반복문 다 돌았다는 건 타깃이 리스트 바깥 수라는 뜻이니까. return first도 ok
    """
            
#테스트코드
if __name__ == "__main__":
    searchInsert([1,3,5,6], 5) #output: 2
    searchInsert([1],3) #output: 2
    searchInsert([1,2,6,9], 0) #output: 0
