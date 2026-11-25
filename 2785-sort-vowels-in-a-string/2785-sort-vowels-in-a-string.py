
class Solution(object):
    def sortVowels(self, s):
        vowels = []

        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)

        vowels.sort()

        result = []
        j = 0

        for ch in s:
            if ch in "aeiouAEIOU":
                result.append(vowels[j])
                j += 1
            else:
                result.append(ch)

        return "".join(result)
