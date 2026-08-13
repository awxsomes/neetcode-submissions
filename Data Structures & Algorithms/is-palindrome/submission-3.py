class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)-1


        while start < end:
            while not (s[start].isalnum()):
                start+=1
                if start > len(s)-1:
                    return True
            while not (s[end].isalnum()):
                end-=1
                if end <0:
                    return True
            print(s[start], s[end])
            if s[start].lower() != s[end].lower():
                return False
            start +=1
            end -=1
            
        return True