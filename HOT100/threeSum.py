"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    双指针+排序 解决

    执行用时 :
    796 ms
    , 在所有 python 提交中击败了
    42.11%
    的用户
    内存消耗 :
    14.9 MB
    , 在所有 python 提交中击败了
    72.79%
    的用户

    边界条件处理麻烦
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        if len(nums) < 3:
            return ret

        last_match = []
        for cnt, num in enumerate(nums):
            start_num = cnt
            end_num = len(nums) - 1
            if cnt > 0 and num == nums[cnt-1]: # 两个连续的值一致的情况
                continue
            if end_num - start_num <= 1:
                break
            while True:
                poor = nums[start_num+1]
                rich = nums[end_num]
                if end_num-start_num == 1:
                    break
                if num + poor + rich == 0:
                    if last_match and last_match == [num, poor, rich]: # 避免匹配到重复的结果
                        end_num -= 1
                        continue
                    if last_match and last_match != [num, poor, rich]:
                        last_match = [num, poor, rich]
                        ret.append([num, poor, rich])
                        end_num -= 1
                    if not last_match:
                        ret.append([num, poor, rich])
                        last_match = [num, poor, rich]
                        end_num -= 1
                elif num + poor + rich > 0:
                    end_num -= 1
                else:
                    start_num += 1
        return ret


if __name__ == '__main__':
    S = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 1, 0, 0, 0 ,0 ]
    ss = S.threeSum(nums)
    print(ss)


# import re
#
# element = '<2.5 HC'
#
# element = re.sub('[,，%]', '', element) if re.search('\d', element) and not re.search("[\u4e00-\u9fa5]+", element) else 0
# if element != 0:
#     element = re.search('\d+.?\d?', element)
#     element = element.group(0)
# print(element)
