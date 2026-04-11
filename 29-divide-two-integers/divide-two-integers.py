class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        
        # Edge case
        if dividend == -2**31 and divisor == -1:
            return INT_MAX
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        result = 0
        
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                result += (1 << i)
                a -= (b << i)
        
        return sign * result