"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix)
        row_index = 0
        move_step = len(matrix) - 1
        max_xy = len(matrix) - 1
        while True:
            if left == right or left > right: 
                break
            for j in range(left, right):
                if j == right-1:
                    continue
                # 当前第一个点的坐标是
                start_site = (row_index, j)
                # 计算出当前点移动时第一次的dx，dy
                if (j + move_step) > right-1:
                    dy = right-1-j
                else: 
                    dy = move_step
                dx = move_step - dy
                current_site_value = matrix[start_site[0]][start_site[1]]
                for x in range(4):
                    # 每个点连续移动四次
                    # 先增加x，再增加y， 再减少x，再减少y
                    if x == 0: 
                        next_site = (start_site[0]+dx, start_site[1]+dy)                
                    elif x == 1:
                        next_site = (start_site[0]+dy, start_site[1]-dx)
                    elif x == 2: 
                        next_site = (start_site[0]-dx, start_site[1]-dy)
                    else:
                        next_site = (start_site[0]-dy, start_site[1]+dx)
                    next_site_value = matrix[next_site[0]][next_site[1]]
                    matrix[next_site[0]][next_site[1]] = current_site_value
                    current_site_value = next_site_value  
                    start_site = next_site              
            left += 1
            right -= 1
            row_index += 1
            move_step -= 2
        return matrix

if __name__ == "__main__":
    S = Solution()
    matrix =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
    m  = [
        [15, 13, 2, 5], 
        [14, 3, 4, 1], 
        [12, 6, 8, 9], 
        [16, 7, 10, 11]
        ]
    ans = S.rotate(matrix)
    print(ans)
