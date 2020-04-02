class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        dq = []
        min_num = min(candidates)
        times = target // min_num
        return self.dfs(candidates, ans, target, dq, times, 0)

    
    def dfs(self, candidates, ans, target, dq, times, n):
        """
        """
        if n == times:
            return ans 

        for num in candidates: 
            if num > target:
                dq.clear() 
                self.dfs(candidates, ans, target, dq, times, n)
            elif num == target: 
                ans.append(dq)
                dq.clear
                self.dfs(candidates, ans, target, dq, times, n)
            else: 
                self.dfs(candidates, ans, target, dq, times, n+1)
                target = target - num
                dq.append(num)
                self.dfs(candidates, ans, target, dq, times, n+1)
        return ans

if __name__ == "__main__":
    S = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    S.combinationSum(candidates, target)