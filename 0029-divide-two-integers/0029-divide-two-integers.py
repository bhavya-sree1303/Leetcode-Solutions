
class Solution(object):
    def divide(self, dividend, divisor):

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a = abs(dividend)
        b = abs(divisor)

        result = 0

        while a >= b:
            temp = b
            count = 1

            while a >= (temp << 1):
                temp = temp << 1
                count = count << 1

            a = a - temp
            result = result + count

        if (dividend < 0) != (divisor < 0):
            result = -result

        return result
