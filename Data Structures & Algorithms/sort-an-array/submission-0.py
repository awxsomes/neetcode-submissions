class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        sortLeft = self.sortArray(left)
        sortRight = self.sortArray(right)
        return self.merge(sortLeft,sortRight)
        
    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j+=1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged