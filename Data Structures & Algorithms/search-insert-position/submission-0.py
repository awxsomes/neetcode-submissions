class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        n = 0
        if target > nums[-1]:
            return end+1
        if target < nums[0]:
            return 0
        while start < end and n<5:
            print(start, mid, end)
            if start == end:
                return start
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
                mid = (start+end)//2
            else:
                end = mid
                mid =(start+end)//2
            n+=1

        return end