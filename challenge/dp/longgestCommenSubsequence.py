"""
给定两个字符串，求这两个字符串的公告最长子序列长度
"""

def lcs(seq1, seq2):
    # 动态转移方程
    # dp[i+1][j+1] = dp[i][j] + 1
    # dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    sub_seq = [[""]*(len(seq2)+1) for _ in range(len(seq1)+1)]
    for cnt_i, i in enumerate(seq1):
        for cnt_j, j in enumerate(seq2):
            if i == j: 
                sub_seq[cnt_i+1][cnt_j+1] = sub_seq[cnt_i][cnt_j] + i
            else:
                sub_seq[cnt_i+1][cnt_j+1] = max(sub_seq[cnt_i+1][cnt_j], sub_seq[cnt_i][cnt_j+1])
    return sub_seq[len(seq1)][len(seq2)]

if __name__ == "__main__":
    seq1 = "abcd"
    seq2 = "aecd"
    print(lcs(seq1, seq2))
