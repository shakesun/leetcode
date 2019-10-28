"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxArea(self, height):
        """
        思路: 双指针法，从两边开始，移动高度较低的指针
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        for _ in range(len(height)):
            h_i = height[i]
            h_j = height[j]
            if h_j > h_i:
                area = h_i * (j-i)
            else:
                area = h_j * (j-i)
            if max_area < area:
                max_area = area
            if h_i > h_j:
                j -= 1
            else:
                i += 1
        return max_area


if __name__ == '__main__':
    S = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = S.maxArea(height)
    print(max_area)
