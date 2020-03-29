class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        distance = [[1e10]*len(grid[0]) for _ in range(len(grid))]
        max_distance = -1
        dxys = [(1,0), (0,1), (-1,0), (0,-1)]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if x == 2 and y == 3:
                    print("ww")
                if grid[x][y] == 1:
                    mark = [[False]*len(grid[0]) for _ in range(len(grid))]
                    que = [(x,y)]
                    distance[x][y] = 0
                    while que:
                        _x, _y = que.pop(0)
                        # if grid[x][y] == "1":
                        for dx, dy in dxys:
                            nx = _x+dx
                            ny = _y+dy
                            if  len(grid) > nx >= 0 and len(grid[x]) > ny >= 0 and grid[nx][ny] != 1 and not mark[nx][ny]: 
                                mark[nx][ny] = True
                                if distance[nx][ny] > distance[_x][_y] + 1: 
                                    distance[nx][ny] = distance[_x][_y] + 1
                                que.append((nx,ny))
        print(distance)
        for i in distance:
            for j in i: 
                if j == 1e10 or j == 0:
                    continue
                else:
                    max_distance = max(max_distance, j)
        
        return max_distance

if __name__ == "__main__":
    S = Solution()
    grid =[
        [0,0,1,1,1],
        [0,1,1,0,0],
        [0,0,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,1]]
    ret = S.maxDistance(grid)
    print(ret)