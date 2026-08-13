class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s):
            
            if s[i] in t:
                t = t.replace(s[i], "" , 1)
                s = s.replace(s[i], "" , 1)
                
                i-=1
            i+=1

        if s == "" and t == "":
            return True
        return False