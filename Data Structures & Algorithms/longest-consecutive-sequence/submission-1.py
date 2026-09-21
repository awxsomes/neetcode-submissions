class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        longest = 0
        for i in numss:
            if i-1 not in numss:
                curr = 1
                while (i+curr) in numss:
                    curr += 1
                longest = max(longest, curr)
        return longest

