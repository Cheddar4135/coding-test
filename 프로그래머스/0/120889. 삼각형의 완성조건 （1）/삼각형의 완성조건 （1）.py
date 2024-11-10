def solution(sides):
    sides=sorted(sides)
    return 1 if sides[2]<(sides[0]+sides[1]) else 2

def solution(sides):
    sides.sort()
    return 1 if sides[2]<(sides[0]+sides[1]) else 2

"""
Q. 파이썬 sort()는 O(nlogn)의 복잡도 필요한데, 안쓰는게 낫지 않아?
A. 어차피 sides는 [변길이1,변길이2,변길이3] 3개의 원소만을 담는 리스트야. 어떤 경우든 O(1)이지. 걍 써.
""" 
