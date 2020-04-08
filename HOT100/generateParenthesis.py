"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
"""


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 随着n的增加，有效括号的数目增加速度本就很快
        # 如何找到n个括号m排列的通解
        # 性质
        # 栈 队列 树 字典 集合 链表
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans

if __name__ == "__main__":
    S = Solution()
    n = 3
    ans = S.generateParenthesis(3)
    print(ans)
