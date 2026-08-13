class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, best= 0, 0, 0

        currwindow = set()

        while r < len(s):
            while s[r] in currwindow and l<r:
                currwindow.remove(s[l])
                l += 1
            currwindow.add(s[r])
            best = max(best, len(currwindow))
            print(s[r])
            print(currwindow)
            
            r+=1
        return best