class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        roman_to_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            cval=roman_to_int[s[i]]
            nval=roman_to_int[s[i+1]] if i+1 < len(s) else 0
            if cval<nval:
                total = total - cval
            else:
                total = total + cval
        return total