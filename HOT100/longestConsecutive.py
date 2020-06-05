class Solution:
    def longestConsecutive(self, nums):

        if not nums:
            return 0
        ans = 1
        tmp_list = set(nums)
        for tmp in tmp_list:
            if tmp-1 not in tmp_list: 
                tmp_ans = 1
                current_tmp = tmp
                while current_tmp + 1 in tmp_list: 
                    tmp_ans += 1
                    current_tmp += 1
                ans = max(ans, tmp_ans)
        return ans



if __name__ == "__main__":
    S = Solution()
    nums = [10, 1, 15, 2, 4, 3]

    ans = S.longestConsecutive(nums)
    print(ans)
