class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, r = 0, 0 ,len(nums)-1

        def swap(uno, dos):
            temp = nums[uno]
            nums[uno] = nums[dos]
            nums[dos] = temp

        while m <= r:
            if nums[m] == 0:
                swap(l,m)
                l += 1
            elif nums[m] == 2:
                swap(m,r)
                m -=1
                r -=1 
            m +=1

        