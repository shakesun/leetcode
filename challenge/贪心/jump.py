"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jump_times = 0
        end = 0
        next_step = 0
        
        for i in range(len(nums)-1):
            if next_step >= i:
                next_step = max(next_step, nums[i]+i)
                if i == end:
                    jump_times += 1
                    end = next_step
        
        return jump_times


