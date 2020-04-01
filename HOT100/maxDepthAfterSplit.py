"""
给你一个「有效括号字符串」 seq，请你将其分成两个不相交的有效括号字符串，A 和 B，并使这两个字符串的深度最小。
"""
class Solution(object):
    # def maxDepthAfterSplit(self, seq):
    #     """
    #     :type seq: str
    #     :rtype: List[int]
    #     """
    #     dq = []
    #     depths = [-1]*len(seq)
    #     max_depths = 0
    #     for i, _ in enumerate(seq): 
    #         if not dq: 
    #             dq.append((i, _))
    #             continue 
    #         if dq[-1][1] == "(" and _ == ")":
    #             left = dq.pop(-1)
    #             depth = len(dq)
    #             if depth > max_depths: 
    #                 max_depths = depth
    #             depths[i], depths[left[0]] = depth, depth
    #         else:
    #             dq.append((i, _))

    #     split_depths = max_depths//2
    #     ans = []
    #     for j, depth in enumerate(depths): 
    #         if depth <= split_depths:
    #             ans.append(0)
    #         else:
    #             ans.append(1)
    #     return ans

     def maxDepthAfterSplit(self, seq):
        """
        根据深度奇偶去选择，不用进行两次遍历
        :type seq: str
        :rtype: List[int]
        """
        dq = []
        ans = [-1]*len(seq)
        for i, _ in enumerate(seq): 
            if not dq: 
                dq.append((i, _))
                continue 
            if dq[-1][1] == "(" and _ == ")":
                left = dq.pop(-1)
                if len(dq)%2 == 1:
                    ans[i], ans[left[0]] = 1, 1
                else:
                    ans[i], ans[left[0]] = 0, 0
            else:
                dq.append((i, _))

        return ans


if __name__ == "__main__":
    S = Solution()
    s = ""
    ans = S.maxDepthAfterSplit(s)
    print(ans)
