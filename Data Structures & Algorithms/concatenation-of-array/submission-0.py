class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num = nums.copy()
        for i in nums:
            num.append(i)
        return num
        