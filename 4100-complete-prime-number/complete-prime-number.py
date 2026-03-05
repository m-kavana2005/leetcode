class Solution(object):
    def completePrime(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = str(num)
        n = len(s)

        for length in range(1, n + 1):
            prefix = int(s[:length])
            suffix = int(s[n - length:])
            if not self.isPrime(prefix) or not self.isPrime(suffix):
                return False
        return True

    def isPrime(self, x):
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True