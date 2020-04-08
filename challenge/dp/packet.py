# 有n个重量和价值分别为wi，vi的物品，从这些物品中挑选出重量不超过W的物品
# 求所有挑选方案中价值总和的最大值

# 1. 暴力求解，每个物品都有选择与不选择两种状态，使用DFS
def dfs(weight, article, n=0, value=0, max_value=0):
    """
    pass
    """
    if value>max_value:
        max_value = value
    if n == len(article):
        # 已经挑选到了最后的一个物品:
        return max_value
    # 当前物品的重量
    weight_n = article[n][0]
    if weight-weight_n < 0:
        # 剩余的重量已经不足以挑选当前物品了
        max_value = dfs(weight, article, n+1, value, max_value)
    else:
        max_value = dfs(weight, article, n+1, value, max_value)
        max_value = dfs(weight-article[n][0], article, n+1, value+article[n][1], max_value)

    return max_value

# 2. 方便记忆优化的深搜
def dfs_plus(weight, article, n):

    if len(article) == n: 
        return 0
    elif weight < article[n][0]:
        ans = dfs_plus(weight, article, n+1)
    else:
        ans = max(dfs_plus(weight, article, n+1), dfs_plus(weight-article[n][0], article, n+1) + article[n][1])
    return ans

# 3. 不方便记忆化搜素的深搜
def _dfs_plus(weight, article, n, summ, dq):
    # TODO 为什么说这种方式使得记忆化搜索难以实现？ 
    if len(article) == n: 
        return summ
    elif weight < article[n][0]:
        ans = _dfs_plus(weight, article, n+1, summ, dq)
    else:
        ans = max(_dfs_plus(weight, article, n+1, summ, dq), _dfs_plus(weight-article[n][0], article, n+1, summ+article[n][1], dq))
    dq[n][weight] = ans
    print(dq)
    return ans


# 3. 记忆优化
def dfs_mem(weight, article, n, dq):

    if dq[n][weight] > 0:
        return dq[n][weight]
    if len(article) == n: 
        return 0
    elif weight < article[n][0]:
        ans = dfs_plus(weight, article, n+1)
    else:
        ans = max(dfs_plus(weight, article, n+1), dfs_plus(weight-article[n][0], article, n+1) + article[n][1])
    dq[n][weight] = ans
    return ans

# 4. 动态规划 1
def dp1(weight, article):

    dq = [[0]*(weight+1) for _ in range(len(article)+1)]
    for a in range(len(article)):
        for w in range(weight+1):
            if article[a][0] > w:
                dq[a+1][w] = dq[a][w]
            else:
                dq[a+1][w] = max(dq[a][w], dq[a][w-article[a][0]]+article[a][1])
    return dq[len(article)][weight]

# 5. 动态规划 2
# def dp2(weight, article):

#     dq = [[0]*(weight+1) for _ in range(len(article)+1)]
#     for a in range(-len(article), 0):
#         for w in range(weight+1):
#             if article[a][0] > w:
#                 dq[a][w] = dq[a+1][w]
#             else:
#                 dq[a][w] = max(dq[a+1][w], dq[a+1][w-article[a][0]]+article[a][1])
#     print(dq)
#     return dq[0][weight]

# 6. 动态规划 3
def dp3(weight, article):

    dq = [0]*(weight+1) 
    for a in range(len(article)):
        for w in range(weight, article[a][0]-1, -1):
            dq[w] = max(dq[w], dq[w-article[a][0]]+article[a][1])
    return dq[weight]

if __name__ == "__main__":
    
    weight = 5
    article = [(2,3), (1,2), (3,4), (2,2)]
    
    # ans = dfs(weight, article)

    # 定义记忆数组
    # dq = [[-1]*(weight+1) for _ in range(len(article)+1)]
    # ans = dfs_mem(weight, article, 0, dq)
    # ans = dfs_plus(weight, article, 0, dq)
    # ans = dfs(weight, article)
    # ans = dp1(weight, article)
    # ans = dp2(weight, article)
    ans = dp3(weight, article)
    # [[-1, -1, -1, -1, -1, 7], [-1, -1, -1, 7, -1, 6], [-1, -1, 7, 7, 6, 6], [7, 6, 7, 5, 4, 2], [-1, -1, -1, -1, -1, -1]]
    # [[-1, -1, -1, -1, -1, 7], [-1, -1, -1, 4, -1, 6], [-1, -1, 2, 4, 4, 6], [0, 0, 2, 2, 2, 2], [-1, -1, -1, -1, -1, -1]]
    print(ans)
