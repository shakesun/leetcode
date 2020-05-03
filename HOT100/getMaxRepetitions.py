class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        # 获取S1 与 S2
        S1 = s1 * n1
        S2 = s2 * n2
        # print(S1)
        # print(S2)
        len_S2 = len(S2)-1
        index = 0
        ans = 0
        for s in S1: 
            if s == S2[index]:
                index += 1
            if index == len_S2:
                ans += 1
                index = 0 
        
        return ans

if __name__ == "__main__":
    S = Solution()

    s1 ="phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf"
    n1 = 1000000
    s2 ="xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly"
    n2 = 100
    ans = S.getMaxRepetitions(s1, n1, s2, n2)
    print(ans)
