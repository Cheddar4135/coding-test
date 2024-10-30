class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = defaultdict(int)
        q = []
        
        for c in s:
            cnt[c] +=1
        for i,c in enumerate(s):
            if cnt[c] == 1:
                return i
        else: return -1
