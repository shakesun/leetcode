
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_ = 0
        same_s_cnt = 0
        same_s_set = set()
        biggest_len = 0
        while True:
            for _s in s[start_:]:
                same_s_cnt += 1
                same_s_set.add(_s)
                if len(same_s_set) != same_s_cnt or same_s_cnt == len(s) or start_+same_s_cnt == len(s):
                    for _ in range(len(same_s_set)):
                        if s[start_:][_] == _s:
                            start_ += _ + 1
                            break
                    if len(same_s_set) > biggest_len:
                        biggest_len = len(same_s_set)
                    same_s_cnt = 0
                    same_s_set.clear()
                    break
            if start_ + biggest_len >= len(s):
                break

        return biggest_len


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         # 初始化子指针和最大长度，不需要额外的匹配子串
#         left = 0
#         max_l = 0
#         for i in range(len(s)):
#             if s[i] in s[left:i]:
#                 left += s[left:i].index(s[i])+1
#             # 长度为两指针间的字符数量
#             l = i - left + 1
#             if l > max_l:
#                 max_l = l
#         return max_l


if __name__ == '__main__':
    S = Solution()
    s = "abcb"
    biggest_len = S.lengthOfLongestSubstring(s)
    print(biggest_len)
