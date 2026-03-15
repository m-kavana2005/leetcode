class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        m=0
        for i in range(0,len(colors)):
            for j in range(len(colors)-1,0,-1):
                if colors[i]!=colors[j] and j>i:
                    m=max(m,j-i)
        return m