from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(rows):
            for j in range(cols):
                # When we find land, process it using BFS
                if grid[i][j] == 1:
                    currArea = 1
                    grid[i][j] = 0  # SINK IT IMMEDIATELY (acts as marking visited)
                    queue = deque([[i, j]])
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in directions:
                            new_r, new_c = curr_r + dr, curr_c + dc
                            
                            # Boundary check and verify it's still land
                            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                                grid[new_r][new_c] = 0  # Sink it before enqueuing to prevent duplicates
                                currArea += 1
                                queue.append([new_r, new_c])
                                
                    maxArea = max(maxArea, currArea)
                    
        return maxArea
