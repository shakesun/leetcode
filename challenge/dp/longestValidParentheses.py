"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 暴力求解试试，找到所有的子串，逐个判断
        # max_val = 0
        # for x in range(len(s)):
        #     for y in range(x+2, len(s)+1):
        #         if self.is_legal(s[x:y]) and y - x > max_val:
        #             max_val = y - x

        # 动态规划解决
        if not s:
            return 0
        dq = [0]*len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dq[i] = dq[i-2] + 2
                elif s[i-dq[i-1]-1] == "(" and i-dq[i-1] > 0:
                    dq[i] = dq[i-1] + dq[i-dq[i-1]-2]+2

        return max(dq)

    def is_legal(self, sub_s): 
        # 判断是否是合法的括号序列
        num = 0
        for _ in sub_s:
            if _ == ")":
                num -= 1
            else:
                num += 1
            if num < 0:
                return False
        return num == 0