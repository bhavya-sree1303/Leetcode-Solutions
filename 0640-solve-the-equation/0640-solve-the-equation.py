
class Solution(object):
    def solveEquation(self, equation):
        left, right = equation.split('=')

        def calculate(s):
            x_count = 0
            number = 0
            sign = 1
            i = 0

            while i < len(s):
                if s[i] == '+':
                    sign = 1
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1
                else:
                    j = i
                    while j < len(s) and s[j].isdigit():
                        j += 1

                    if j < len(s) and s[j] == 'x':
                        coefficient = int(s[i:j]) if j > i else 1
                        x_count += sign * coefficient
                        i = j + 1
                    elif s[i] == 'x':
                        x_count += sign
                        i += 1
                    else:
                        number += sign * int(s[i:j])
                        i = j

            return x_count, number

        left_x, left_num = calculate(left)
        right_x, right_num = calculate(right)

        x = left_x - right_x
        num = right_num - left_num

        if x == 0:
            if num == 0:
                return "Infinite solutions"
            return "No solution"

        return "x=" + str(num // x)
