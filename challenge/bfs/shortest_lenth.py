# 给定一个大小为N*M的迷宫，”#“表示墙壁，”.“表示通道，每一步可以上下左右移动
# 假设存在迷宫存在解，求出通过迷宫的最短路径， 入口为”S“，出口为”G“


INF = 1e10
destance = [ [1e10]*5 for i in range(6)]
dxy = [(1,0), (0,1),(-1,0), (0,-1)]
destance[0][1]=0
def bfs(maze): 
    que = [(0,1)]
    while que: 
        x, y = que.pop(0)
        if maze[x][y] == "G": 
            break

        for dx, dy in dxy:
            nx = x+dx 
            ny = y+dy 
    
            if len(maze) > nx >= 0 and len(maze[0]) > ny >= 0 and maze[nx][ny] != "#" and destance[nx][ny] == 1e10:
                que.append((nx,ny))
                destance[nx][ny] = destance[x][y]+1

    return destance[x][y]

if __name__ == "__main__":
    maze = [
        ["#", 'S', '.', "#", "#"],
        ["#", "#", '.', "#", "#"],
        [".", '.', '.', ".", "#"],
        [".", '#', '#', ".", "#"],
        [".", '.', '.', ".", "#"],
        ["#", '#', '#', "G", "#"],
    ]
    print(bfs(maze))
    [[10000000000.0, 0, 1, 10000000000.0, 10000000000.0],
     [10000000000.0, 10000000000.0, 2, 10000000000.0, 10000000000.0], 
     [5, 4, 3, 4, 10000000000.0],
      [6, 10000000000.0, 10000000000.0, 11, 10000000000.0], 
      [7, 8, 9, 10, 10000000000.0],
       [10000000000.0, 10000000000.0, 10000000000.0, 11, 10000000000.0]]