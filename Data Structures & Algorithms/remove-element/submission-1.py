class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums) -1
        i = 0
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        count = 0
        while i <= size:
            print(i, size)
            print(nums)
            
            if nums[i] == val:
                swap(i, size)
                
                size -= 1
            else:
                i += 1
                count += 1
        return count