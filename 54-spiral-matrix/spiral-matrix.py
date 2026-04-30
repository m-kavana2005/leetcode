class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        t=l=0
        r = len(matrix[0])-1
        b = len(matrix)-1
        while l<=r and t<=b:
            for j in range(l,r+1):
                res.append(matrix[t][j])
            t += 1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if t<=b:
                for j in range(r,l-1,-1):
                    res.append(matrix[b][j])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res