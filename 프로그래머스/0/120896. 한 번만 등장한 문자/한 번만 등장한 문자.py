from collections import Counter
def solution(s):
    # abcabcadc
    # 각 문자 나온 횟수 count하기
    # value가 1인 key만 저장하고 정렬하기
    count = Counter(s)
    keys = list(count.keys())
    values = list(count.values())
    
    return ''.join(sorted([keys[i] for i in range(len(values)) if values[i]==1]))