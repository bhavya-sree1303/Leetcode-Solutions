class Solution(object):
    def findBall(self, grid):
        m = len(grid)
        n = len(grid[0])

        answer = []

        for start in range(n):
            col = start

            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction

                if next_col < 0 or next_col >= n:
                    col = -1
                    break

                if grid[row][next_col] != direction:
                    col = -1
                    break

                col = next_col

            answer.append(col)

        return answer