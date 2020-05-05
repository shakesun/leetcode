"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
"""

# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         # 贪心的思路，每一次跳跃都选择跳到能跳到最远的地方去
#         if not nums: 
#             return True
#         max_jump = nums[0]

#         def sub(start, max_jump):
#             if max_jump >= len(nums) - 1:
#                 return True
#             if start == max_jump + 1:
#                 return False
#             if start == max_jump and nums[start] == 0:
#                 return False
#             new_max_jump = max_jump
#             new_start = 0
#             for i in range(start, max_jump + 1):
#                 tmp_jump = nums[i] + i
#                 if tmp_jump >= new_max_jump:
#                     new_start = i
#                     new_max_jump = tmp_jump
#             return sub(new_start, new_max_jump)

#         return sub(1, max_jump)

class Solution:
    def canJump(self, nums):
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

    