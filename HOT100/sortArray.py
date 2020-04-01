class Solution(object):

    # 1. 选择排序
    # def sortArray(self, nums):
    #     """
    #     O(n²)超时
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     for i, n1 in enumerate(nums):
    #         min_index = i
    #         min_num = n1
    #         for j in range(i, len(nums)):
    #             if min_num > nums[j]: 
    #                 min_num = nums[j]
    #                 min_index = j
    #         nums[i], nums[min_index] = nums[min_index], nums[i]
    #     return nums

    # 2. 归并排序
    def sortArray(self, nums):
        if len(nums) < 2:
            return nums

        minddle = len(nums)//2
        left = nums[:minddle]
        right = nums[minddle:]

        return self.merge_sort(self.sortArray(left), self.sortArray(right))
    def __init__(self):

        self.sorted_nums = []

    def merge_sort(self, left, right):

        if left and right:
            if left[0] >= right[0]:
                self.sorted_nums.append(right.pop(0))
            else:
                self.sorted_nums.append(left.pop(0))
        if left:
            self.sorted_nums.append(left.pop(0))
        if right:
            self.sorted_nums.append(right.pop(0))
        return self.sorted_nums

    # 计数排序
    def cnt_sort(self, nums): 
        max_num = max(nums)
        min_num = min(nums)

        cnt_list = [[i, None] for i in range(min_num, max_num+1)]
        for num in nums:
            cnt_index = num-min_num
            if not cnt_list[cnt_index][1]: 
                cnt_list[cnt_index][1] = 1
            else: 
                cnt_list[cnt_index][1] = cnt_list[cnt_index][1] + 1
        
        sorted_nums = []
        for cnt in cnt_list: 
            num = cnt[0]
            times = cnt[1]
            if not times: 
                continue
            else:
                sorted_nums += [num]*times

        return sorted_nums


if __name__ == "__main__":
    nums = [-4,0,7,4,9,-5,-1,0,-7,-1]
    S = Solution()
    # num = S.cnt_sort(nums)
    num = S.sortArray(nums)
    print(num)
