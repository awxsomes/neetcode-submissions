class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = 0
        for i in nums:
            if count == 0:
                cand = i
                count += 1
            elif i == cand:
                count += 1
            elif i != cand:
                count -= 1
        return cand