class Solution1(object):
    """内存消耗比较厉害"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        for cnt, num in enumerate(nums):
            index_dict[num] = cnt

        for cnt, num in enumerate(nums):
            need_key = target - num
            if need_key in index_dict.keys() and cnt != index_dict[need_key]:
                return cnt, index_dict[need_key]

        # 相同的思路，细节处理的更好，所以速度更快
        # _dict = {}
        # for i, m in enumerate(nums):
        #     _dict[m] = i
        #
        # for i, m in enumerate(nums):
        #     j = _dict.get(target - m)
        #     if j is not None and i != j:
        #         return [i, j]

        return None


if __name__ == "__main__":
    S = Solution1()
    nums = [3, 2, 4]
    target = 6
    ss = S.twoSum(nums, target)
    print(ss)
