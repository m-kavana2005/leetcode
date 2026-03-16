class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        x = sorted(heights)[::-1]
        a = []
        for i in x:
            a.append(names[heights.index(i)])
        return a