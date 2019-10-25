"""
题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
import time

class Solution(object):

    def longestPalindrome(self, s):
        """
        时间复杂度为O(n3)，比较垃圾
        :type s: str
        :rtype: str
        """
        longest = ''
        longest_len = 0
        for cnt in range(len(s)):
            for cnt_, _s in enumerate(s):
                cnt_ += 1
                if cnt_ <= cnt:
                    continue
                part_s = s[cnt: cnt_]
                if self.isPalindrome(part_s):
                    if longest_len < len(part_s):
                        longest = part_s
                        longest_len = len(part_s)
        return longest

    def isPalindrome(self, s):
        """
        判断以当前字符串是否为回文字串
        通过判断是否对称来判断是否是回文字串
        :param s:
        :return:
        """
        if len(s) % 2:
            for _ in range(len(s)//2):
                if s[_] != s[-(_+1)]:
                    return False
            return True
        else:
            for _ in range(len(s) // 2):
                if s[_] != s[-(_+1)]:
                    return False
            return True

    # def longestPalindrome(self, s):
    #     """
    #     时间复杂度为O(n3)，比较垃圾
    #     :type s: str
    #     :rtype: str
    #     """
    #     longest = ''
    #     longest_len = 0
    #     for cnt in range(len(s)):
    #
    #         pass
    #     return longest


if __name__ == '__main__':
    S = Solution()
    s = "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"
    t1 = time.time()
    print(S.longestPalindrome(s))
    t2 = time.time()
    print(t2-t1)

