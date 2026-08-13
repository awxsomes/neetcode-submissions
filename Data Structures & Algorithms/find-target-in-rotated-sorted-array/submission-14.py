class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1

        while l <= h:
            mid = l+(h-l)//2

            if nums[mid] == target:
                return mid
            if nums[h] >= nums[mid]:
                if target > nums[mid] and target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
            else:
                if target < nums[mid] and target >= nums[l]:
                    h = mid-1
                else:
                    l = mid+1

        return -1


