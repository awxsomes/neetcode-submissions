class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [row[0] for row in matrix]

    
        l, h = 0, len(first_col)-1
        while l <= h:
            mid = l + (h - l) // 2
            print(mid)
            print(l)
            print(h)
            if first_col[mid] == target:
                return True
            elif first_col[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        print(mid)
        row = matrix[h]
        print(row)
        l, h = 0, len(row)-1
        while l <= h:
            mid = l + (h-l)//2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                h = mid - 1
            else:
                return True
        return False

        
        
        