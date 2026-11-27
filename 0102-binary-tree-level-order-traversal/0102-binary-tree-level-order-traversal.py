
from collections import deque

class Solution(object):
    def levelOrder(self, root):

        result = []

        if root is None:
            return result

        q = deque()
        q.append(root)

        while q:

            size = len(q)
            level = []

            for i in range(size):

                current = q.popleft()

                level.append(current.val)

                if current.left is not None:
                    q.append(current.left)

                if current.right is not None:
                    q.append(current.right)

            result.append(level)

        return result
