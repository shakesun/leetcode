from functools import lru_cache

# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         N = len(days)
#         durations = [1, 7, 30]

#         @lru_cache(None)
#         def dp(i):
#             if i >= N:
#                 return 0
#             ans = 10**9
#             j = i
#             for c, d in zip(costs, durations):
#                 while j < N and days[j] < days[i] + d:
#                     j += 1
#                 ans = min(ans, dp(j) + c)
#             return ans

#         return dp(0)


class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        mem = [0]*366
        days_set = set(days)
        for i in range(1, days[-1]+1):
            if i not in days_set:
                mem[i] = mem[i-1]
            else:
                mem[i] = min(mem[i-1]+costs[0], mem[i-7]+costs[1], mem[i-30]+costs[2])
                
        return mem[days[-1]]
