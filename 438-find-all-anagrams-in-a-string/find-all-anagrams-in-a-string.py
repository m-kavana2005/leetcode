class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_count = [0]*26
        window = [0]*26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        k = len(p)

        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1

            if i >= k:
                window[ord(s[i-k]) - ord('a')] -= 1

            if window == p_count:
                res.append(i - k + 1)

        return res