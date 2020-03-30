def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)


if __name__ == "__main__":
    S = Solution()
    n = 5
    m = 3
    ans = S.lastRemaining(n, m)
    print(ans)