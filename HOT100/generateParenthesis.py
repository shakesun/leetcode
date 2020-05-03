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

# 自己的解法，比较笨拙，判断括号是否有效使用了栈
class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        Parenthesis = []
        allBracketStr = []
        perStr = ""
        allBracketStr = self.generateAllBracketStrByFor(n)
        for brackets in allBracketStr:
            if self.is_good_bracket(brackets):
                Parenthesis.append(brackets)
        # print(Parenthesis)
        return Parenthesis

    def is_good_bracket(self, brackets):
        """
        判断是否是合法的括号序列
        """
        stack = []
        for s in brackets:
            if len(stack) == 0:
                stack.append(s)
            else:
                if stack[-1] == "(" and s == ")":
                    stack.pop(-1)
                else:
                    stack.append(s)
        if len(stack) == 0:
            return True
        else:
            return False
    
    # 不适用栈判断括号是否有效
    def valid(A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0

    def generateAllBracketStrByFor(self, n):
        """
        生成所有的可能的括号序列 数目为n！
        """
        ret = []
        middle_ret = [""]
        for _ in range(2*n):
            middle_ret = [i + j for i in middle_ret for j in ["(", ")" ]]
        for _ in middle_ret:
            if _.count("(") == n:
                ret.append(_)
        return ret

if __name__ == "__main__":
    S = Solution()
    n = 3
    ans = S.generateParenthesis(3)
    print(ans)
