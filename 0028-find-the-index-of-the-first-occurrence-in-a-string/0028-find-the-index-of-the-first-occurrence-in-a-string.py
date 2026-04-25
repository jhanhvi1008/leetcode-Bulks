class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        # Edge case
        if m > n:
            return -1

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
        