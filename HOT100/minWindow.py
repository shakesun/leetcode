class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        _count_dict = dict()
        repeat_set = set(list(t))
        for _ in t:
            _count_dict[_] = 0
        for _ in t:
            _count_dict[_] += 1
        
        ans = ""
        while True: 
            # print(left)

            if s[right] in repeat_set and not self.contain(_count_dict):
                _count_dict[s[right]] -= 1
            if self.contain(_count_dict) and s[left] in repeat_set:
                print(left)
                if not ans:
                    ans = s[left:right+1]
                elif right-left < len(ans):
                    ans = s[left:right+1]

                _count_dict[s[left]] += 1
                left += 1
            if not self.contain(_count_dict) and right < len(s)-1:
                right += 1
            if right-1 == len(s) and (s[left] in repeat_set and self.contain(self.tmp_coutain(_count_dict, s[left])) or self.contain(_count_dict)):
                break
            if s[left] not in repeat_set and left < len(s):
                left += 1
            print(left)
            print(right)
        return ans

    def contain(self, _count_dict):

        for _ in _count_dict.values():
            if _ > 0:
                return False
        return True
    
    def tmp_coutain(self, _count_dict, left_s):
        _count_dict[left_s] += 1
        return _count_dict

if __name__ == "__main__":
    S = Solution()
    s = "ADOBECODEBANC"
    t = "ABCC"
    ans = S.minWindow(s, t)
    print(ans)
