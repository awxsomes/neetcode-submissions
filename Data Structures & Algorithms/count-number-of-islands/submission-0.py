from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == "1" and not visited[i][j]):
                    visited[i][j] = True
                    queue =deque([[i,j]])
                    while len(queue) > 0:
                        curr = queue.popleft()
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for dr, dc in directions:
                            new_r = curr[0] + dr
                            new_col = curr[1] + dc
                            if (0 <= new_r < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_r][new_col] == "1" and not visited[new_r][new_col]):
                                
                                visited[new_r][new_col] = True
                                queue.append([new_r, new_col])
                    total += 1
        return total