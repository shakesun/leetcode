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
        # return max_value
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

# 2. 记忆优化
def mem_dfs(weight, article, n=0, value=0, max_value=0):
    if n == len(article):
        # 已经挑选到了最后的一个物品:
        # return max_value
        return max_value
    if dq[n][weight-1] != -1: 
        return dq[n][weight]
    if value>max_value:
        max_value = value
    # 当前物品的重量
    weight_n = article[n][0]
    if weight-weight_n < 0:
        # 剩余的重量已经不足以挑选当前物品了
        max_value = mem_dfs(weight, article, n+1, value, max_value)
    else:
        max_value = mem_dfs(weight, article, n+1, value, max_value)
        max_value = mem_dfs(weight-article[n][0], article, n+1, value+article[n][1], max_value)
    dq[n][weight-1] = max_value
    return max_value


if __name__ == "__main__":
    
    weight = 5
    article = [(2,3), (1,2), (3,4), (2,2)]
    
    # ans = dfs(weight, article)

    # 定义记忆数组
    dq = [[-1]*weight for _ in range(len(article))]
    ans = mem_dfs(weight, article)

    print(ans)
