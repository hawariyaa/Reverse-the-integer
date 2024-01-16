# Reverse the integer, if the given integer is out of the 32 bit integer range return 0
# our range is between (2 ** -31) to (2 ** 31) -1
import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        Min = -2147483648
        Max = 2147483647
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > Max // 10 or res == Max // 10 and digit >= Max % 10:
                return 0
            if res < Min // 10 or res == Min and digit <= Min % 10:
                return 0
            res = (res * 10) + digit

        return res * sign
num = -4765
answer = Solution()
output = answer.reverse(num)
print(output)

