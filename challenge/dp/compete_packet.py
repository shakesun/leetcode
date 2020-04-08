#  有n中重量和价值分别为wivi的物品，从中选取重量为W的物品，使得价值最大，同一种物品可以多次选择

def compete_packet_dp1(weight, article):
    
    dq = [[0]*(weight+1) for _ in range(len(article)+1)]

    for i in range(len(article)):
        for j in range(weight+1):
            xx = j//article[i][0]
            for x in range(0 , xx+1):
                dq[i+1][j] = max(dq[i+1][j], dq[i][j-x*article[i][0]]+article[i][1]*x)
    
    print(dq)
    return dq[len(article)][weight]

def compete_packet_dp2(weight, article):

    dq = [[0]*(weight+1) for _ in range(len(article)+1)]

    for i in range(len(article)):
        for j in range(weight+1):
            if j < article[i][0]:
                dq[i+1][j] = dq[i][j]
            else:
                dq[i+1][j] = max(dq[i][j], dq[i+1][j-article[i][0]]+article[i][1])
    return dq[len(article)][weight]


if __name__ == "__main__":
    weight = 7
    article = [(3,4), (4,5), (2,3)]
    ans = compete_packet_dp2(weight, article)
    print(ans)
