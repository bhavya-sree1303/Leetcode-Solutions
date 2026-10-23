
class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        j = 0

        for ch in str1:
            next_ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))

            if j < len(str2) and (ch == str2[j] or next_ch == str2[j]):
                j += 1

        return j == len(str2)
