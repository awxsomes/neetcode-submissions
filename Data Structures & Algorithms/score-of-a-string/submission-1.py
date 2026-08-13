class Solution:
    def scoreOfString(self, s: str) -> int:
        # t = 0
        # for i in range(len(s)-1):
        #     t += abs(ord(s[i])-ord(s[i+1]))
        # return t

        return sum(abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(s)))