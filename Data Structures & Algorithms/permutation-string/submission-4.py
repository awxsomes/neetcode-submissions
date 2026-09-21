from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        look = Counter(s1)
        print(look)
        for r in range(len(s1), len(s2)+1):
            print(s2[l:r])
            if Counter(s2[l:r]) == look:
                return True
            l+=1
        return False