"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        """
        # bfs到n层时候的叶子节点数目 O(m*n)
        
        # dq = [[1]*m for i in range(n)]

        # for i in range(1, n):
        #     for j in range(1, m):
        #         dq[i][j] = dq[i-1][j] + dq[i][j-1]

        # return dq[-1][-1]
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

