import copy
class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # next_board = []
        # next_board.extend(board)
        next_board = copy.deepcopy(board)
        # next_board = list(board)
        dxs = [1,0,-1]
        dys = [1,0,-1]
        for x in range(len(board)):
            for y in range(len(board[x])):
                life = 0
                for dx in dxs:
                    for dy in dys:
                        if dx == dy == 0:
                            continue
                        nx = x+dx
                        ny = y+dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:                         
                            if x==0 and y==2:
                                print("--")
                            life += 1
                # print(life)
                if board[x][y] == 0 and life == 3:
                    next_board[x][y] = 1
                elif board[x][y] == 1 and (life < 2 or life > 3): 
                    next_board[x][y] = 0
                else:
                    next_board[x][y] == board[x][y]
        return next_board

if __name__ == '__main__':
    S = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    ret = S.gameOfLife(board)
    print(ret)
