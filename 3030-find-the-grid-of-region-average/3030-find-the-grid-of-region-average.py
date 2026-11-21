
class Solution(object):
    def resultGrid(self, image, threshold):
        m = len(image)
        n = len(image[0])

        sums = [[0] * n for _ in range(m)]
        count = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):

                valid = True

                # Check horizontal neighbours
                for r in range(i, i + 3):
                    for c in range(j, j + 2):
                        if abs(image[r][c] - image[r][c + 1]) > threshold:
                            valid = False
                            break
                    if not valid:
                        break

                # Check vertical neighbours
                if valid:
                    for r in range(i, i + 2):
                        for c in range(j, j + 3):
                            if abs(image[r][c] - image[r + 1][c]) > threshold:
                                valid = False
                                break
                        if not valid:
                            break

                if valid:
                    total = 0

                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            total += image[r][c]

                    avg = total // 9

                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            sums[r][c] += avg
                            count[r][c] += 1

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if count[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] = sums[i][j] // count[i][j]

        return result
