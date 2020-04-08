class Solution:
    def minDistance(self, word1, word2):
        # 找到最长的匹配数
        max_match = 0
        for i in range(len(word2)):
            match = 0
            for j in range(len(word1)):
                if word1[j] == word2[i]:
                    match += 1
                    range_times = min(len(word2)-i-1, len(word1)-j-1)
                    for x in range(1, range_times+1):
                        if word1[j+x] == word2[i+x]:
                            match += 1
                # 当找到首个匹配的字母后，后面的字母按照位置进行匹配
            max_match = max(max_match, match)
        return len(word2)-max_match

if __name__ == "__main__":
    S = Solution()
    w2 = "intention"
    w1 = "execution"
    ans = S.minDistance(w1, w2)
    print(ans)