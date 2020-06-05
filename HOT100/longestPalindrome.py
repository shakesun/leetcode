"""
题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
import time

class Solution(object):

    # def longestPalindrome(self, s):
    #     """
    #     时间复杂度为O(n3)，比较垃圾
    #     :type s: str
    #     :rtype: str
    #     """
    #     longest = ''
    #     longest_len = 0
    #     for cnt in range(len(s)):
    #         for cnt_, _s in enumerate(s):
    #             cnt_ += 1
    #             if cnt_ <= cnt:
    #                 continue
    #             part_s = s[cnt: cnt_]
    #             if self.isPalindrome(part_s):
    #                 if longest_len < len(part_s):
    #                     longest = part_s
    #                     longest_len = len(part_s)
    #     return longest

    def isPalindrome(self, s):
        """
        判断以当前字符串是否为回文字串
        通过判断是否对称来判断是否是回文字串
        :param s:
        :return:
        """
        if len(s) % 2:
            for _ in range(len(s)//2):
                if s[_] != s[-(_+1)]:
                    return False
            return True
        else:
            for _ in range(len(s) // 2):
                if s[_] != s[-(_+1)]:
                    return False
            return True

    # def longestPalindrome(self, s):
    #     """
    #     时间复杂度为O(n3)，比较垃圾
    #     :type s: str
    #     :rtype: str
    #     """
    #     longest = ''
    #     longest_len = 0
    #     for cnt in range(len(s)):
    #
    #         pass
    #     return longest

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: 
            return s 
        
        dq = [0] * len(s)
        dq_num = 1
        dq[0] = 1
        max_sub = s[0]

        for i in range(1, len(s)):
            if i - dq_num - 1  >= 0 and s[i-dq_num-1] == s[i]:
                dq_num = dq_num + 2
            elif s[i-1] == s[i] and s[i-dq_num+1:i+1].count(s[i]) == len(s[i-dq_num+1:i+1]):
                dq_num += 1
            elif i - dq_num - 1  >= 0 and s[i-2] == s[i]:
                dq_num = 3
            else:
                dq_num = 1
            if dq_num > len(max_sub):
                max_sub = s[i-dq_num+1:i+1]

        return max_sub


if __name__ == '__main__':
    S = Solution()
    s = "ababababa"
    # t1 = time.time()
    print(S.longestPalindrome(s))
    # t2 = time.time()
    # print(t2-t1)

