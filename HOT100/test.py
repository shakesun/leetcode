 
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # ss =  self.minimumLength(words, "")
        # print(ss)
        return len(self.minimumLength(words, ""))

    def minimumLength(self, words, S):
        max_repeat_len = 0
        max_repeat_word = ""
        max_repeat_words = []
        for s in words:
            repeat_len = 0
            repeat_word = []
            for s1 in words:
                if s1 == s[-len(s1):] and s != s1:
                    repeat_word.append(s1)
                    repeat_len += len(s1)
                    if repeat_len > max_repeat_len:
                        max_repeat_words = repeat_word
                        max_repeat_len = repeat_len
                        max_repeat_word = s
        if max_repeat_len == 0:
            for _ in words:
                S += (_+"#")
            return S
        else:
            print("max_rep",max_repeat_word)
            print("rep_w",max_repeat_words)
            for _ in max_repeat_words:
                words.remove(_)
            words.remove(max_repeat_word)
            S += (max_repeat_word+"#")
            print("word", words)
            return self.minimumLength(words, S)

if __name__ == "__main__":
    S = Solution()
    w = ["time", "me", "bell"]
    print(S.minimumLengthEncoding(w))