"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


class Solution(object):

    T_T = """
        官方题解：给出的双指针比单个指针实现要好一些
        具体好在，单指针实现遇到最高点时候反转去做遍历的判断条件使得不得不遍历结束第一次后再反转，这里的步骤在双指针实现是没必要的
        双指针在遇到更高点时候直接变换遍历方向。这里的假设是，你高，你就可能是最高的，我就直接转向，你不是最高的也行，我还能转回来
        
        使用栈的解法也挺好，核心是:将小于栈顶的压入栈，遇到大于栈顶的元素则认为栈顶元素被当前元素与栈顶下面一个元素定义
        
        似乎可以用动态规划解决。。没仔细看
    """

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 1. 找到所有可以盛雨水的区间，
        #   下标不同，高度相同，
        #   或者，高度不同，且高度非零
        #   两柱之间要有凹处
        # 2. 计算凹处的面积

        # 往前嗅探，可能需要回头，所以是两次遍历
        # 怎么继续优化呢？ 两次遍历太多了，，，双指针？

        # 找出各个高点，凹处必然在两高点之间

        # 特殊情况
        if not height:
            return 0

        # 先写一个出来
        # 设定单个指针
        _point = 0
        total_area = 0
        part_area = 0
        index = -1
        while True:
            index += 1
            if _point + 1 == len(height):
                break

            p_h = height[_point]
            i_h = height[index]

            jauge = index - _point
            if jauge == 1 and p_h <= i_h:
                # 下一个与当前指针指向的位置高度相同或者高于，这时候将指针下移一位即可
                _point = index
                continue
            elif jauge >= 1 and p_h >= i_h:
                # 存在下一个柱低于当前指针指向的柱子，有可能是凹处，计算面积, 指针与下标都是不需要改动的
                part_area += 1 * (p_h-i_h)

            if jauge > 1 and p_h <= i_h:
                # 遇到了可以结束的点，可以将凹处的面积增加入总面积
                total_area += part_area
                _point = index
                part_area = 0
                continue

            if index + 1 == len(height) and part_area != 0:
                # 遍历至最后一个柱子没有找到可以与当前指针指向的柱子形成凹槽的柱子，将剩余部分反向查找，返回反向查找得到的面积
                need_reverse_height = height[_point:]
                need_reverse_height.reverse()
                reverse_part_area = self.trap(need_reverse_height)
                total_area += reverse_part_area
                break

        return total_area


if __name__ == '__main__':
    S = Solution()
    heights = []
    area = S.trap(heights)
    print(area)
