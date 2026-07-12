from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1
        # Handle 1 separately
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1
        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt.get(cur, 0) >= 2:
                length += 2
                cur *= cur
            # If current value exists once, use it as the center.
            if cnt.get(cur, 0) == 1:
                length += 1
            else:
                # Otherwise, the previous value can be the center
                length -= 1

            ans = max(ans, length)

        return ans