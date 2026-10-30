class Solution(object):
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        for layer in range(min(m, n) // 2):
            elements = []

            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            for j in range(left, right + 1):
                elements.append(grid[top][j])

            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])

            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            r = k % len(elements)
            elements = elements[r:] + elements[:r]

            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = elements[idx]
                idx += 1

            for i in range(top + 1, bottom + 1):
                grid[i][right] = elements[idx]
                idx += 1

            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = elements[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[idx]
                idx += 1

        return grid