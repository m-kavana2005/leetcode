class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        ans=0
        while n>0:
            ans += 1<< (32-(n&-n).bit_length())
            n&=(n-1)
        return ans