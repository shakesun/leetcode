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


    # 2.计数排序
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


# 3. 归并排序
def merge_sort(collection):

    def merge(left, right):
        '''merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        '''
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result + left + right
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


if __name__ == "__main__":
    nums = [-4,0,7,4,9,-5,-1,0,-7,-1]
    S = Solution()
    # num = S.cnt_sort(nums)
    # num = S.sortArray(nums)
    num = merge_sort(nums)
    print(num)

