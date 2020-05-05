"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 感觉可以用dfs 剪枝解决
        
        ans = []
        def sub_nums(l_num, s_num):
            if len(l_num) == len(nums):
                ans.append(l_num[:])            
            for num in nums:
                if num not in s_num:
                    s_num.add(num)
                    l_num.append(num)
                    sub_nums(l_num, s_num)
                    l_num.pop(-1)
                    s_num.remove(num)
        s = set()
        sub_nums([], s)

        return ans

if __name__ == "__main__":
    S = Solution()
    nums = [1,2,3]
    ans = S.permute(nums)
    print(ans)
