class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(s1,s2):
            while s2:
                s1,s2=s2,s1%s2
            return s1
        if str1 + str2 != str2 + str1:
            return ""
        result = gcd(len(str1),len(str2))
        return str1[:result]
    