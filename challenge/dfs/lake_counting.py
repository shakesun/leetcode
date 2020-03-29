# 有一个n*m的院子，里面有积水，‘W’表示水，‘.’表示无水，求出院子里面有多少水洼？
def dfs(x, y): 
    
    courtyard[x][y] = "."
    for i in range(-1, 2): 
        for j in range(-1, 2): 
            if x+i >= 0 and y+j >= 0 and x+i < len(courtyard) and y+j < len(courtyard[x]): 
                # 没有越界
                if courtyard[x+i][y+j] == "W":
                    # 递归调用
                    return dfs(x+i, y+j)

def counting(courtyard):
    ans = 0
    for x in range(len(courtyard)):
        for y in range(len(courtyard[x])): 
            if courtyard[x][y] == "W": 
                ans += 1
                dfs(x, y)
    
    return ans 

if __name__ == "__main__":
    courtyard = [
        ["W","W",".","W","W"],
        ["W","W",".",".","."],
        [".",".","W",".","."],
        ["W","W",".",".","W"],
        ["W","W",".",".","."]
    ]
    print(counting(courtyard))
