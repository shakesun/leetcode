# 给定整数a1a2,a3,a4...,an,判断是否可以从中选取出若干数，使得它们之和恰好等于k。
k = 15
a = [1,2,3,4,5]

def dfs(i, ans): 
    if i == len(a): 
        return ans == k 
    if dfs(i+1, ans):
        return True
    if dfs(i+1, ans+a[i]):
        return True
    return False

if __name__ == "__main__":
    print(dfs(0,0))
 