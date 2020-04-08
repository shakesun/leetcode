"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def movingCount(self, m, n, k):
        
        metrix = [[-1]*m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                a = i//100
                b = i//10
                c = i%10
                d = j//100
                e = j//10
                f = j%10
                if a+b+c+d+e+f <= k:
                    metrix[i][j] = 0
        print(metrix)
        ans = self.dfs(0, 0, metrix, ans)
        return ans

    def dfs(self, x, y, metrix, ans):
        # 深度优先搜索，从（0，0）开始搜
        ans += 1
        metrix[x][y] = -1
        dxys = [(1,0), (0,1), (-1,0), (0,-1)]
        for dx, dy in dxys:
            nx = x + dx
            ny = y + dy
            if 0<=nx<len(metrix) and 0<=ny<len(metrix[0]) and metrix[nx][ny] == 0:
                ans = self.dfs(nx, ny, metrix, ans)
        return ans 

if __name__ == "__main__":
    S = Solution()
    m = 2
    n = 3
    k = 1
    ans = S.movingCount(m, n, k)
    print(ans)
    