class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newStrs = sorted(strs)

        i = j = 0
        count = ""
        while i < len(newStrs[0]) and j < len(newStrs[-1]):
            if newStrs[0][i] == newStrs[-1][j]:
                count += newStrs[0][i]
                i += 1
                j += 1
            else:
                break
        return count