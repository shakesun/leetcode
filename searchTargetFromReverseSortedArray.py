class Solution:
    def search(self, nums, target):
        # 确定是否在有序的部分就可以了
        left = 0
        right = len(nums)-1
        if not nums:
            return -1

        return self.split_2(left, right, nums, target)

    def split_2(self, left, right, nums, target):
        if left == right or left+1 == right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        mid = (left+right)//2
        if self.is_orders(nums[left:mid+1]):
            # 前半部分有序
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target and nums[left] <= target:
                return self.split_2(left, mid, nums, target)
            else:
                return self.split_2(mid, right, nums, target)

        else:
            if nums[mid+1] == target:
                return mid+1
            elif nums[mid+1] < target and nums[right] >= target: 
                return self.split_2(mid, right, nums, target)
            else:
                return self.split_2(left, mid, nums, target)

    def is_orders(self, l): 
        return l[0] < l[-1]

if __name__ == "__main__":
    S = Solution()
    nums = [5,1,3]
    # nums = [1, 3, 5]
    target = 5
    ans = S.search(nums, target)
    print(ans)
