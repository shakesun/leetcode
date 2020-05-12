class Solution:
    def dailyTemperatures(self, T):
        stack = []
        ans = [0]*len(T)

        left = 0
        for i, j in enumerate(T):
            if i == 0:
                continue
            if j <= T[left]:
                while stack and j > stack[-1][1]:
                    tmp = stack.pop(-1)
                    ans[tmp[0]] = i - tmp[0]
                stack.append((i,j))
            else:
                ans[left] = i - left
                while stack:
                    tmp = stack.pop(-1)
                    ans[tmp[0]] = i - tmp[0]
                left = i
                
        return ans 

if __name__ == "__main__":
    S = Solution()
    T = [73,74,75,71,69,72,76,73]
    ans = S.dailyTemperatures(T)
    print(ans)
