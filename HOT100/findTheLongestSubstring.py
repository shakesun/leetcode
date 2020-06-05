class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 12
        meta_s = set(["a", "o", "e", "i", "u"])
        ans_list = self.helper(s, [], meta_s)
        # print(ans_list)
        return max(ans_list)

    def helper(self, sub_s, ans_list, meta_s):
        # print("递归中")
        # print(ans_list)
        if self.judge(sub_s):
            # print("有结果")
            ans_list.append(len(sub_s))
        if not sub_s:
            print("sss")
            return ans_list
        elif sub_s[0] in meta_s and sub_s[-1] not in meta_s:
            # print("左删除")
            self.helper(sub_s[1:], ans_list, meta_s)
        elif sub_s[-1] in meta_s and sub_s[0] not in meta_s:
            self.helper(sub_s[:len(sub_s)-1], ans_list, meta_s)
        else:
            self.helper(sub_s[1:], ans_list, meta_s)
            self.helper(sub_s[:len(sub_s)-1], ans_list, meta_s)

        return ans_list

    def judge(self,sub_s):
        judge_l = [sub_s.count("a")%2 == 0, sub_s.count("o")%2 == 0,sub_s.count("e")%2 == 0,sub_s.count("i")%2 == 0,sub_s.count("u")%2 == 0]
        if all(judge_l):
            return True
        return False

if __name__ == "__main__":
    S = Solution()
    ss = "leetcodeisgreat"
    ans = S.findTheLongestSubstring(ss)
    print(ans)



