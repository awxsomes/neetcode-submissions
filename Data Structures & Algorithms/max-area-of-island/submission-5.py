from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        maxArea = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    currArea = 1 
                    visited[i][j] = True
                    queue = deque([[i, j]])
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in directions:
                            new_r, new_c = curr_r + dr, curr_c + dc
                            
                            if (0 <= new_r < rows and 
                                0 <= new_c < cols and 
                                grid[new_r][new_c] == 1 and 
                                not visited[new_r][new_c]):
                                
                                visited[new_r][new_c] = True
                                currArea += 1
                                queue.append([new_r, new_c])
                                
                    maxArea = max(maxArea, currArea)
        return maxArea
