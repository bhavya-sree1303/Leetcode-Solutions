class Solution(object):
    def arrayRankTransform(self, arr):
      sorted_unique = sorted(set(arr))
      rank = {num: i + 1 for i, num in enumerate(sorted_unique)}
      return [rank[x] for x in arr]