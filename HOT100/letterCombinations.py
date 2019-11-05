"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""


class Solution(object):
    """
    抄袭的大佬写法，妙啊！
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_str_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        ls1 = ['']
        for num in digits:
            ls1 = [x + y for x in ls1 for y in num_str_mapping[num]]

        return ls1


if __name__ == '__main__':
    digits = '232'
    S = Solution()
    ss = S.letterCombinations(digits)
    print(ss)
