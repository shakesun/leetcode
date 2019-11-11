"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    T_T = """
    开始的思路是，用字典去匹配左右，但是并不知道怎么解决括号顺序导致非法的情况
    
    1. 找解决方案而不是找问题所在
    
    未想到的原因分析：
    对有效括号没有理解到递归结构的层面。合法输入的最内层必然是一对有效的括号。
    没有联想到用栈去做处理
    """

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_dict = {
            "(": ')',
            "{": "}",
            "[": "]"
        }
        ls1 = []
        if not s:
            return True
        if s[0] not in map_dict.keys():
            return False

        for _ in s:
            if _ in map_dict.keys():
                # 匹配到左括号，压入栈
                ls1.append(_)
            else:
                # 匹配到右括号，取出栈顶元素。
                if not ls1:
                    return False
                if map_dict[ls1[-1]] == _:
                    # 如果与栈顶括号匹配，将栈顶元素弹出
                    ls1.pop(-1)
                else:
                    return False

        if len(ls1) != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    S = Solution()
    s = "[])"
    if S.isValid(s):
        print('合法')
    else:
        print("不合法")
