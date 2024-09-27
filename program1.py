class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Boundary conditions and checking if the current cell is water ('W')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current cell as visited (we can change 'L' to 'W')
            grid[r][c] = 'W'
            
            # Visit all 4 neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        island_count = 0

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ('L'), this is a new island
                if grid[r][c] == 'L':
                    island_count += 1  # Increment island count
                    dfs(r, c)  # Start DFS to mark the entire island as visited

        return island_count

# Example usage:
solution = Solution()

# Dispatch 1
grid1 = [["L", "L", "L", "L", "W"], ["L", "L", "W", "L", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "W", "W", "W"]]
print(solution.getTotalIsles(grid1))  # Output: 1

# Dispatch 2
grid2 = [["L", "L", "W", "W", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "L", "W", "W"], ["W", "W", "W", "L", "L"]]
print(solution.getTotalIsles(grid2))  # Output: 3
