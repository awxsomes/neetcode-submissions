class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1, 2, 3, 4, 5, 6, 7]
        # [4, 5, 6, 7, 1, 2, 3]
        # [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]

        l, h = 0, len(nums)-1

        while l <= h:
            mid = l+(h-l)//2

            if nums[h] > nums[mid]:
                h = mid
            elif nums[l] < nums[mid]:
                l = mid
            else:
                return nums[h]