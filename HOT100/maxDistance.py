"""
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？
请返回该海洋区域到离它最近的陆地区域的距离。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        distance = [[1e10]*len(grid[0]) for _ in range(len(grid))]
        max_distance = -1
        dxys = [(1,0), (0,1), (-1,0), (0,-1)]
        que = []
        for x in range(len(grid)):
            for y in range(len(grid[x])): 
                if grid[x][y] == 1:
                    que.append((x, y))
                    distance[x][y] = 0
        if not que or len(que) == len(grid)*len(grid[0]): 
            return -1
        while que:
            _x, _y = que.pop(0)
            for dx, dy in dxys:
                nx = _x+dx
                ny = _y+dy
                if len(grid) > nx >= 0 and len(grid[x]) > ny >= 0 and grid[nx][ny] != 1 and distance[nx][ny] == 1e10: 
                    distance[nx][ny] = distance[_x][_y] + 1
                    grid[nx][ny] = 1
                    que.append((nx,ny))

        return distance[_x][_y]


if __name__ == "__main__":
    S = Solution()
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    ret = S.maxDistance(grid)
    print(ret)