class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        match = not not s and s[0] == p[0]
        return match and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    S = Solution()
    s = "aa"
    p = "aa"
    ans = S.isMatch(s, p)
    print(ans)
