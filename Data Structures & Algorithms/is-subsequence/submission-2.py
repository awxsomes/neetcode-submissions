class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==""):
            return True
        s_curr = 0
        for i in t:
            if s[s_curr] == i:
                s_curr += 1
            if s_curr == len(s):
                return True
            
            
        return False
        