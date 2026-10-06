class Solution(object):
    def divisibilityArray(self, word, m):
        answer = []
        remainder = 0

        for digit in word:
            remainder = (remainder * 10 + int(digit)) % m

            if remainder == 0:
                answer.append(1)
            else:
                answer.append(0)

        return answer