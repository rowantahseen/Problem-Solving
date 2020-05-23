class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        l_s1 = len(s1)
        l_s2 = len(s2)

        if l_s2 >= l_s1:        
            for i in range(l_s2-l_s1+1):
                if s1_count == Counter(s2[i:i+l_s1]): return True
        return False
