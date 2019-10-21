"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = self._combine_two_list(nums1, nums2, combined_nums=[])
        # print(nums)
        if len(nums) % 2:
            return nums[len(nums)//2]
        else:
            return float((nums[len(nums)//2-1] + nums[len(nums)//2])/2.0)

    def _combine_two_list(self, nums1, nums2, combined_nums=[]):
        """
        递归处理
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) == 0:
            combined_nums.extend(nums2)
            return combined_nums

        if len(nums2) == 0:
            combined_nums.extend(nums1)
            return combined_nums

        num1 = nums1[0]
        num2 = nums2[0]
        if num1 > num2:
            combined_nums.append(num2)
            del nums2[0]
        else:
            combined_nums.append(num1)
            del nums1[0]

        return self._combine_two_list(nums1, nums2, combined_nums=combined_nums)


if __name__ == '__main__':
    S = Solution()
    nums1 = [3, 4]
    nums2 = [1, 2]
    ret = S.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(ret)
