class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # i = 0
        # while i < len(s):
            
        #     if s[i] in t:
        #         t = t.replace(s[i], "" , 1)
        #         s = s.replace(s[i], "" , 1)
                
        #         i-=1
        #     i+=1

        # if s == "" and t == "":
        #     return True
        # return False


        if len(s) != len(t):
            return False

        first, second = {}, {}

        for i in range(len(s)):
            first[s[i]] = 1 + first.get(s[i], 0)
            second[t[i]] = 1 + second.get(t[i],0)

        if first == second:
            return True
        return False